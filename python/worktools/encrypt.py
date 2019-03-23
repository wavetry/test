#!/usr/python
# coding=utf-8

import os,sys,json,getopt,shutil,time
from logUtil import exec_cmd

def encryptLua(src,dst):
	exec_cmd("cocos luacompile -s %s -d %s -k 20180309zslm -b 20180309zslm -e --disable-compile" % (src,dst))

def encryptPng(src,dst):
	with open(src,'rb+') as f:
		content = f.read()
		size = len(content)
		for i in range(size):
			print(content[i])
			if i % 1024 == 1:
				content[i] = hex(content[i]) ^ 0x00
			if i % 1024 == 10:
				content[i] = hex(content[i]) ^ 0xa0
			if i % 1024 == 30:
				content[i] = hex(content[i]) ^ 0xb1
			if i % 1024 == 427:
				content[i] = hex(content[i]) ^ 0xc2
			if i % 1024 == 521:
				content[i] = hex(content[i]) ^ 0xd3
			# print(k,char)
		# print(content)
		with open(dst,'wb+') as fd:
			fd.write(content)
			fd.flush()

# encryptPng('test.png','test1.png')
# encryptLua("E:/project/client_dw/src/","E:/project/client_dw/src1/")
