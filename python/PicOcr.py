# #!/usr/bin/env python
# # -*- coding:utf-8 -*-

import pytesseract
from PIL import Image,ImageFilter,ImageFilter,ImageDraw
import re,sys,getopt,os
reload(sys)
sys.setdefaultencoding('utf8')

file_list = []

#二值判断,如果确认是噪声,用改点的上面一个点的灰度进行替换
#该函数也可以改成RGB判断的,具体看需求如何
def getPixel(image,x,y,G,N):
    L = image.getpixel((x,y))
    if L > G:
        L = True
    else:
        L = False

    nearDots = 0
    if L == (image.getpixel((x - 1,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1,y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1,y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x,y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y + 1)) > G):
        nearDots += 1

    if nearDots < N:
        return image.getpixel((x,y-1))
    else:
        return None

# 降噪 
# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点 
# G: Integer 图像二值化阀值 
# N: Integer 降噪率 0 <N <8 
# Z: Integer 降噪次数 
# 输出 
#  0：降噪成功 
#  1：降噪失败 
def clearNoise(image,G,N,Z):
    draw = ImageDraw.Draw(image)

    for i in xrange(0,Z):
        for x in xrange(1,image.size[0] - 1):
            for y in xrange(1,image.size[1] - 1):
                color = getPixel(image,x,y,G,N)
                if color != None:
                    draw.point((x,y),color)

def initTable(threshold=140):           # 二值化函数
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table

def is_contain_cn(picPath):
	cnpattern = re.compile(u'[\u4e00-\u9fa5]+')
	image = Image.open(picPath)
	width, height = image.size
	image = image.resize((width * 4, height * 4)) 
	

	# for i in range(width * 2):
	#     for j in range(height * 2):
	#         try:
	#             r,g,b,alpha = image.getpixel((i,j))
	#             image.putpixel((i,j), (255 - r,255 - g,255 - b,255 - alpha))
	#         except Exception as e:
	#             continue 
	image = image.convert('L')
	# image = image.point(initTable(), '1')                    #3.降噪，图片二值化
	image = image.filter(ImageFilter.EDGE_ENHANCE)
	# clearNoise(image,50,4,4)
	
	# image.save(picPath)

	code = pytesseract.image_to_string(image, lang='chi_sim',config="-psm {}".format(14))
	print(code)

	hasCn = cnpattern.search(code)
	if hasCn:
		image.show()
	return hasCn

def search(path):
	dirs_files = os.listdir(path)
	for file_name in dirs_files:
		full_path = os.path.join(path,file_name)
		full_path = unicode(full_path) #ascii to unicode
		if os.path.isdir(full_path):
			search(full_path)
		else:
			file_ext = file_name.split(".")[-1]
			if file_ext == "png" or file_ext == "jpg":
				if is_contain_cn(full_path):
					# print(full_path)
					file_list.append(full_path)


if __name__ == '__main__':
	try:
		reload(sys)
		sys.setdefaultencoding('utf-8')
		root_path = raw_input('input file path:')
		root_path = unicode(root_path) #ascii to unicode

		# windows
		# root_path = root_path.replace('/','\\')
		#linux
		root_path = root_path[:-1]

		argv = sys.argv
		try:
			opts, args = getopt.getopt(argv[1:], 'hvp:', ['path='])
		except getopt.GetoptError:
			sys.exit(2)
		for o, a in opts:
			if o in ('-p', '--path'):
				root_path = a
		# print file_list
		if None != root_path:
			search(root_path)
		# file_list.sort(reverse=True)
		for obj in file_list:
			print (obj)
		print("total Num:",len(file_list))
		raw_input('Press Enter to exit...')
	except:
		print ("Unexpected error:", sys.exc_info()) # sys.exc_info()返回出错信息
		raw_input('press enter key to exit') #这儿放一个等待输入是为了不让程序退出


# from PIL import Image
# import pytesseract
# from pytesseract import *

# rep={'O':'0',                           #替换列表
#     'I':'1','L':'1',
#     'Z':'2',
#     'S':'8'
#     };

# def initTable(threshold=140):           # 二值化函数
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)

#     return table
# #--------------------------------------------------------------------------------------
# im = Image.open('/Users/wavetry/SVN/develop0.3.1/CCB/Resources/ccbResources/tongyong/tongyong_title/ty_title_01.png')     #1.打开图片
# im = im.convert('L')                                        #2.将彩色图像转化为灰度图
# binaryImage = im.point(initTable(), '1')                    #3.降噪，图片二值化
# binaryImage.show()

# text = image_to_string(binaryImage,lang='chi_sim' , config='-psm 7')

# #4.对于识别结果，常进行一些替换操作
# for r in rep:
#     text = text.replace(r,rep[r])

# #5.打印识别结果
# print(text)