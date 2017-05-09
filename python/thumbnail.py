#!/usr/bin/env python
# coding=utf-8

import os,sys
from PIL import Image,ImageFilter

ext_files = []
ext_strings = []


def get_attribute_value(node,attribute_name):
	return node.getAttribute(attribute_name) if node else ''

def get_xml_node(node,name):
	return node.getElementsByTagName(name) if node else[]

def read_xml(path):
	#解析xml
	print(path)
	doc = minidom.parse(path)
	#得到根节点
	root = doc.documentElement
	#读取跟节点对应的信息
	imagePath = root.getAttribute("imagePath")
	print (imagePath)
	new_file_name = imagePath.split(".")[0]
	
	image_file_dir = path.split("\\")
	image_file_path = ""
	for index,item in enumerate(image_file_dir):
		if index == len(image_file_dir) - 1:
			break;
		if index == 0:
			image_file_path = ("%s\\")%(item)
		elif index == len(image_file_dir) -2:
			image_file_path = ("%s%s\\")%(image_file_path,item)
		else:
			image_file_path = ("%s%s\\")%(image_file_path,item)
	new_file_path = ("%s%s")%(image_file_path,new_file_name)
	print (new_file_path)
	if os.path.exists(new_file_path) == True:
		os.mkdir(new_file_path)
	image_file_path = ("%s%s")%(image_file_path,imagePath)	
	print(image_file_path)
	
	#子节点中的信息，ImageName，x,y,width,height
	subTexture_nodes = get_xml_node(root,'SubTexture')
	for node in subTexture_nodes:
		name = get_attribute_value(node,'name')
		x = get_attribute_value(node,'x')
		y = get_attribute_value(node,'y')
		width = get_attribute_value(node,'width')
		height = get_attribute_value(node,'height')
		
		name = ("%s.png")%(name)
		x = x.encode("utf-8")
		y = y.encode("utf-8")
		width = width.encode("utf-8")
		height = height.encode("utf-8")
		name = name.encode("utf-8")
		
		left = int(x)
		upper = int(y)
		right = int(x) + int(width)
		lower = int(y) + int(height) 


def  filter_file(path,ext):
	dirs_files = os.listdir(path)
	for file_name in dirs_files:
		full_path = os.path.join(path,file_name)
		if os.path.isdir(full_path):
			filter_file(full_path,ext)
		file_ext = file_name.split(".")[-1]
		if ext != file_ext:
			continue
		print(full_path)	
		ext_files.append(full_path)
	# with open('pic.txt','a+') as f :
	# 	f.write("\n".join(ext_files))

if __name__ == '__main__': 
	path = sys.path[0]
	ext = 'plist'
	try:
		os.remove('pic.txt')
	except OSError, e:
		print "no such file but now creating"
	
	filter_file(path,ext)
	print ("Done")
