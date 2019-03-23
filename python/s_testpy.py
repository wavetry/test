#!/usr/python
# coding=utf-8
def fa(x):
	if not isinstance(x,(int ,float)):
		raise TypeError('error')
	if x <=1:
		return 1	
	else:
		return x


def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

##**kw means dictionary 
# def person(name,age,**kw):
# 	print('name:', name, 'age:', age, 'other:', kw)

# #和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# def man(name, *,age):
# 	print(name,age)

#递归
def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n - 1)
#递归会溢出,可以用尾递归优化
def factx(n):
	return fact_iter(n,1)
def fact_iter(num,pro):
	if num == 1:
		return pro
	return fact_iter(num - 1,num * pro)
#汉诺塔问题

def move(n,a,b,c):
	if n==1:
		print('move',a,'-->',c)
		return
	move(n-1,a,c,b)
	print('move',a,'-->',c)
	move(n-1,b,a,c)

#斐波那契数列
def fbnc(n):
	if n==1 or n==0:
		return n
	return fbnc(n-1)+fbnc(n-2)

#杨辉三角
def triangles1():
	b = [1]
	i=0
	while True:
		yield b
		b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
		print(b)

def triangles2():
    L=[1,]
    while(True):
        yield L 
        i=len(L)-1
        while(i):
            L[i]=L[i]+L[i-1]
            i-=1
        L.append(1)
# n=0
# for t in triangles2():
#     print (t)
#     n=n+1
#     if n==10:
#         break

from functools import reduce
def str2float(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(lambda x,y:x*10+y,map(char2num,s.replace('.','')))/(10**s[::-1].find('.') if s.find('.')!=-1 else 1)

def _odd_iter():
	n=1
	while True:
		n+=2
		yield n

def _not_divisible(n):
	return lambda x:x%n>0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n=next(it)
		yield n
		it = filter(_not_divisible,it)
#文件读写 'r'read 'rb'read in binary 'w'write 'wb'write in binary
# with open('test.lua','r',encoding = 'gbk',errors = 'ignore') as f:
# 	print(f.read(100))
# 	# for lines in f.readlines():
# 	# 	print(lines.strip())

# with open('test.txt','w',encoding = 'utf-8')as f:
# 	f.write('Hello Woarld')


# def by_name(t):
# 	return t[0].lower()
# def by_score(t):
# 	return t[1]
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=by_name)
# print(L2)
# L2 = sorted(L, key=by_score,reverse=True)
# print(L2)

# [x for x in os.listdir('.') if os.path.isdir(x)]
# [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#json
# import json

# class Student(object):
# 	def __init__(self, name, age, score):
# 		self.name = name
# 		self.age = age
# 		self.score = score
	
# def student2dict(std):
# 		return {
# 	    	'name': std.name,
# 	    	'age': std.age,
# 	    	'score': std.score
# 	    	}
# s = Student('Bob', 20, 88)
# print(json.dumps(s, default=student2dict))

# print(json.dumps(s, default=lambda s: s.__dict__))

# '''
# 遍历当前目录及其子目录下文件名包含指定字符串的文件的绝对路径
# '''
# import os
# def fun(name,path='.',res=set([])):
#     path = os.path.abspath(path)
#     L = os.listdir(path)
#     for x in L:
#         tpath = os.path.join(path,x)
#         if os.path.isfile(tpath):
#             if name in os.path.split(os.path.splitext(tpath)[0])[1]:
#                 res.add(tpath)
#         elif os.path.isdir(tpath):
#             fun(name,tpath,res)
#     return res

# L = fun('work')
# for x in L:
# 	print (x)

# #client tcp
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('127.0.0.1',9999))
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
# 	s.send(data)
# 	print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()
# #server udp
# #!/usr/bin/env python
# #_*_ coding:utf-8 _*_
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(("127.0.0.1",9999))
# print("Bind UDP on 9999")
# while True:
# 	data,addr = s.recvfrom(1024)
# 	print("Received from %s:%s." % addr)
# 	s.sendto(b'Hello,%s!' % data,addr)

#-*- coding: utf-8 -*-
# from PIL import Image,ImageDraw,ImageFont 0000

# originl_avatar = "test.jpg"
# save_avatar = "new_avatar.jpg"
# windows_font = "Arial.ttf"
# color = (255,0,0)

# def draw_text(text,fill_color,windows_font):
# 	print("do some")
# 	try:
# 		im = Image.open(originl_avatar)
# 		x,y = im.size
# 		print(im.size,im.format,im.mode)
# 		im.show()

# 		draw = ImageDraw.Draw(im)
# 		font = ImageFont.truetype(windows_font,35)
# 		draw.text((x - 20,7),text,fill_color,font)
# 		im.save(save_avatar)
# 		im.show()
# 	except :
# 		print("Unable to load Image")


# number = str("4")
# draw_text(number,color,windows_font)

# #生成随机密钥
# # -*- coding: utf-8 -*- 0001
# import random,string
# import MySQLdb

# db = MySQLdb.connect("localhost","root","964711246lzl","coupon")
# cursor = db.cursor()


# class LengthError(ValueError):
# 	"""docstring for LengthError"""
# 	def __init__(self, arg):
# 		super(LengthError, self).__init__()
# 		self.arg = arg
# def pad_zero_to_left(inputNumString,totalLength):
# 	lengthOfInput  = len(inputNumString)
# 	if lengthOfInput > totalLength:
# 		raise LengthError("error")
# 	else:
# 		return '0' * (totalLength - lengthOfInput) + inputNumString

# poolOfChars = string.ascii_letters + string.digits
# random_codes = lambda x,y:''.join([random.choice(x) for i in range(y)])

# def invitation_code_generator(quantity,lengthOfRandom,LengthOfKey):
# 	placeHoldChar = "L"
# 	for index in range(quantity):
# 		tempString = ""
# 		try:
# 			yield random_codes(poolOfChars, lengthOfRandom) + placeHoldChar + pad_zero_to_left(str(index), LengthOfKey)
# 		except LengthError:
# 			print "Index exceeds the length of master key."

# for invitationCode in invitation_code_generator(200,10,4):
#     sql = """INSERT INTO table1(coupon)
#             VALUE ('%s')
#         """ % invitationCode
    
#     try:
#         cursor.execute(sql)
#         db.commit()
#         print( sql)
#     except Exception, e:
#         print(e)
#         db.rollback()
# db.close()


	
# from multiprocessing import Pool 
# import os,time,random

# def long_time_task(name):
# 	print("Run task %s (%s) ..." % (name,os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print("Task %s runs %0.2f seconds." % (name , (end - start)))

# if __name__ == '__main__':
# 	print ("Parent process %s." % os.getpid())
# 	p = Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_time_task,args=(i,))
# 	print("Waiting for all subprocessed done...")
# 	p.close()
# 	p.join()
# 	print('All subprocessed done')


# import subprocess

# print('nslookup')
# r = subprocess.call(['ls'])
# print('Exit code:',r)

# import subprocess

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# from multiprocessing import Process,Queue
# import os,time,random

# def write(q):
# 	print('Process to write :%s' % os.getpid())
# 	for value in ['A','B','C']:
# 		print('Put %s to Queue ...' % value)
# 		q.put(value)
# 		time.sleep(random.random())
# def read(q):
# 	print ('Process to read %s ' % os.getpid())
# 	while True:
# 		value = q.get(True)
# 		print('Get %s from queue' % value)




# if __name__ == '__main__':
# 	q = Queue()
# 	pw = Process(target=write,args = (q,))
# 	pr = Process(target=read,args = (q,))
# 	pw.start()
# 	pr.start()
# 	pw.join()
# 	pr.terminate()


# import time,threading

# def loop():
# 	print('thread %s is running ...' % threading.current_thread().name)
# 	n = 0
# 	while n < 5 :
# 		n = n + 1
# 		print('thread %s >>> %s' % (threading.current_thread().name,n))
# 		time.sleep(1)
# 	print('thread %s ended' % threading.current_thread().name)

# print('thread %s is running ...' % threading.current_thread().name)
# t = threading.Thread(target=loop)
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


import time, threading

# 假定这是你的银行存款:
balance = 0

lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
    	lock.acquire()
    	try:
    		change_it(n)	
    	finally:
    		lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#下载歌词
import os
import os.path
import re
import eyed3
import urllib2
import urllib
from urllib import urlencode
import sys 
import os
reload(sys) 
sys.setdefaultencoding('utf8')
 
music_path = r"/Users/youai/Music/网易云音乐"
lrc_path = r"/Users/youai/Music/网易云音乐/lrc"
 
os.remove('nolrc.txt')
os.remove('lrcxml.txt')
 
the_file = open('lrcxml.txt','a')
nolrc_file = open('nolrc.txt','a')

 
for root,dirs,files in os.walk(music_path):
    for filepath in files:
        the_path = os.path.join(root,filepath)
        if (the_path.find("mp3") != -1):
            print the_path
            the_music = eyed3.load(the_path)
            the_teg = the_music.tag._getAlbum()
            the_artist = the_music.tag._getArtist()
            the_title = the_music.tag._getTitle()
           # print the_teg
           # print the_title
           # print the_artist
            b = the_title.replace(' ','+')
           # print b
            a = the_artist.replace(' ','+')
            #print urlencode(str(b))
            if isinstance(a,unicode):
                a = a.encode('utf8')
            song_url = "http://box.zhangmen.baidu.com/x?op=12&count=1&title="+b+"$$"+a+"$$$$ "
 
            the_file.write(song_url+'\n')
            page = urllib2.urlopen(song_url).read()
            print page
            theid = 0
 
            lrcid =  re.compile('<lrcid>(.*?)</lrcid>',re.S).findall(page)
            have_lrc = True
            if lrcid != []:
                theid = lrcid[0]
 
            else:
                nolrc_file.write(the_title+'\n')
                have_lrc = False
            print theid
 
            if have_lrc:
                firstid = int(theid)/100
                lrcurl = "http://box.zhangmen.baidu.com/bdlrc/"+str(firstid)+"/"+theid+".lrc"
                print lrcurl
                lrc = urllib2.urlopen(lrcurl).read()
                if(lrc.find('html')== -1):
                    lrcfile = open(lrc_path+"\\"+the_title+".lrc",'w')
                    lrcfile.writelines(lrc)
                    lrcfile.close()
                else:
                    nolrc_file.write(the_title+'\n')
 
the_file.close()
nolrc_file.close()
print "end!"


# from PIL import Image

# # 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('test.png')
# # 获得图像尺寸:
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# # 缩放到50%:
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# im.save('thumbnail.jpg', 'jpeg')

# from PIL import Image,ImageFilter
# im = Image.open('test.png')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg','jpeg')



#生成验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(127, 255), random.randint(127, 255), random.randint(127, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# s = input('insert string:\n')
# n=len(s)
# # 240 x 60:
# width = 60 * n
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('/Library/Fonts/Microsoft/STXINWEI.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# i=0
# for t in s:
    
#     draw.text((60 * i + 10, 10), t, font=font, fill=rndColor2())
#     i=i+1
# # 模糊:
# image = image.filter(ImageFilter.CONTOUR)
# name = ("%s.jpg"%s)
# image.save(name, 'jpeg')
