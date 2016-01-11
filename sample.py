#下载歌词
# import os
# import os.path
# import re
# import eyed3
# import urllib2
# import urllib
# from urllib import urlencode
# import sys 
# import os
# reload(sys) 
# sys.setdefaultencoding('utf8')
 
# music_path = r"/Users/youai/Music/网易云音乐"
# lrc_path = r"/Users/youai/Music/网易云音乐/lrc"
 
# os.remove('nolrc.txt')
# os.remove('lrcxml.txt')
 
# the_file = open('lrcxml.txt','a')
# nolrc_file = open('nolrc.txt','a')

 
# for root,dirs,files in os.walk(music_path):
#     for filepath in files:
#         the_path = os.path.join(root,filepath)
#         if (the_path.find("mp3") != -1):
#             print the_path
#             the_music = eyed3.load(the_path)
#             the_teg = the_music.tag._getAlbum()
#             the_artist = the_music.tag._getArtist()
#             the_title = the_music.tag._getTitle()
#            # print the_teg
#            # print the_title
#            # print the_artist
#             b = the_title.replace(' ','+')
#            # print b
#             a = the_artist.replace(' ','+')
#             #print urlencode(str(b))
#             if isinstance(a,unicode):
#                 a = a.encode('utf8')
#             song_url = "http://box.zhangmen.baidu.com/x?op=12&count=1&title="+b+"$$"+a+"$$$$ "
 
#             the_file.write(song_url+'\n')
#             page = urllib2.urlopen(song_url).read()
#             print page
#             theid = 0
 
#             lrcid =  re.compile('<lrcid>(.*?)</lrcid>',re.S).findall(page)
#             have_lrc = True
#             if lrcid != []:
#                 theid = lrcid[0]
 
#             else:
#                 nolrc_file.write(the_title+'\n')
#                 have_lrc = False
#             print theid
 
#             if have_lrc:
#                 firstid = int(theid)/100
#                 lrcurl = "http://box.zhangmen.baidu.com/bdlrc/"+str(firstid)+"/"+theid+".lrc"
#                 print lrcurl
#                 lrc = urllib2.urlopen(lrcurl).read()
#                 if(lrc.find('html')== -1):
#                     lrcfile = open(lrc_path+"\\"+the_title+".lrc",'w')
#                     lrcfile.writelines(lrc)
#                     lrcfile.close()
#                 else:
#                     nolrc_file.write(the_title+'\n')
 
# the_file.close()
# nolrc_file.close()
# print "end!"


#生成验证码
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import random

# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))

# # 随机颜色1:
# def rndColor():
#     return (random.randint(127, 255), random.randint(127, 255), random.randint(127, 255))

# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# s = input('insert string:\n')
# n=len(s)
# # 240 x 60:
# width = 60 * n
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('/Library/Fonts/Libian.ttc', 36)
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
# image = image.filter(ImageFilter.BLUR)
# name = ("%s.jpg"%s)
# image.save(name, 'jpeg')