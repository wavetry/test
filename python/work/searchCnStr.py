#!/usr/bin/env python
# coding=utf-8
import os, re, shutil, json, sys, getopt, datetime, time, base64

startIndex = 196
result_str=[]
cnpattern = re.compile(u'[\S]+[\"].[\u4e00-\u9fa5]+.[\"]')
cnpattern1 = re.compile(u'[\"].[\u4e00-\u9fa5]+.[\"]')
cnpattern2 = re.compile(u'print\([\"].[\u4e00-\u9fa5]+.[\"]')
cnpattern3 = re.compile(u'dump\([\S]+[\"].[\u4e00-\u9fa5]+.[\"]')
cnpattern4 = re.compile(u'--[.]*[\"].[\u4e00-\u9fa5]+.[\"]')

fileObject = open('TipConfig.txt', 'w')  

def replace_ch(target_path):
	global startIndex
	global fileObject
	global result_str
	fd = open(target_path,mode='r', encoding='UTF-8')
	txt = fd.read()
	txt = txt.decode("utf-8")
	fd.close()

	# r = u'([一-龥]+)'
	
	result = cnpattern.findall(txt)
	for item in result:
		# print cnpattern2.search(item)
		if cnpattern2.search(item) == None and cnpattern3.search(item) == None and cnpattern4.search(item) == None:
			item1 = cnpattern1.findall(item)[0]
			print (item1)
			txt = txt.replace(item1, "TipConfig[%d]" % startIndex)
			result_str.append("[%d] = %s"  % (startIndex,item1) )
			startIndex = startIndex + 1
	txt = txt.encode('utf-8')

	if len(result_str) > 0:
		newstr = ",\n".join(result_str) + ",\n"
		result_str = []
		newstr = newstr.encode('utf-8')
		fileObject.write(newstr)  
		if None != txt and 0 < txt.__len__():
			fd = open(target_path, 'w')
			fd.write(txt)
			fd.flush()
			fd.close()
		print("".join(result))
	

def get_file(path,ext):
	dirs_files = os.listdir(path)
	files = []
	for item_name in dirs_files:
		full_path = os.path.join(path,item_name)
		if os.path.isdir(full_path):
			continue
		file_ext = item_name.split(".")[-1]
		if ext != file_ext:
			continue

		file_stat = os.stat(full_path)
		obj = [item_name, full_path , file_stat]
		files.append(obj)

	return files


def search(path,ext):
	dirs_files = os.listdir(path)

	for file_name in dirs_files:
		full_path = os.path.join(path,file_name)
		if os.path.isdir(full_path):
			search(full_path,ext)
		file_ext = file_name.split(".")[-1]
		if ext != file_ext:
			continue
		# print(file_name,file_name.find("Config"))
		if file_name.find("Config") == -1:
			replace_ch(full_path)


if __name__ == "__main__":
	global fileObject
	root_path = u'E:\\project\\client_dw\\src\\app\\utils\\'
	root_path = u'E:\\project\\client_dw\\src\\'
	# root_path = u'C:\\test\\'

	# root_path = unicode(root_path) #ascii to unicode
	# root_path = root_path.replace('/','\\')
	print("root_path",root_path)
	try:
		os.remove('TipConfig.txt')
	except OSError, e:
		print "no such file named TipConfig.txt but now creating"
	if None != root_path:
		search(root_path,"lua")
	fileObject.close()