#-*- coding: UTF-8 -*-
print 'ToFng start ..'  
import os, time, sys, hashlib, json, codecs, shutil, struct
# from base64 import b64encode
# if can't find Image,use cmd "sudo pip install image"
from PIL import Image, ImageDraw, ImageFont, ImageFilter

with open('E:\\project\\client_dw\\win32\\juhao\\res\\resource\\act_6.png','rb+') as fd:
	imgRaw = fd.read()
	i = 0
	newRaw = ""
	for char in imgRaw:
		i = i + 1
		if i%1024 == 1:
			char = int(ord(char)) ^ 0x00
		elif i % 1024 == 10:
			char = int(ord(char)) ^ 0xa0
		elif i % 1024 == 30:
			char = int(ord(char)) ^ 0xb1
		elif i % 1024 == 427:
			char = int(ord(char)) ^ 0xc2
		elif i % 1024 == 521:
			char = int(ord(char)) ^ 0xd3
		newRaw = newRaw + str(char)
	with open("E:\\project\\client_dw\\win32\\juhao\\res\\resource\\act_7.png",'w+') as fr:
		fr.write(newRaw)
