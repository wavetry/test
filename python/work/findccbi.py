#!/usr/bin/env python
# coding=utf-8
import os,re
def findccbi(path,ext):
	dirs_files = os.listdir(path)
	script_files = []
	script_strings = []
	script_files_map = {}
	for file_name in dirs_files:
		full_path = os.path.join(path,file_name)
		if os.path.isdir(full_path):
			findccbi(full_path,ext)
		file_ext = file_name.split(".")[-1]
		if ext != file_ext:
			continue
		file_stat = os.stat(full_path)
		obj = [file_name,full_path,file_stat,ext]
		script_files.append(obj)

		with open(full_path,'r') as f:
			res = re.search(r'ccbi\/\S+'ccbi,f.read())
			if res:
				script_strings.append(file_name + "-----" + res.group(0))
	result =  "\n".join(script_strings)
	with open('ccbiInfo.txt','a+') as f :
		f.write(result)

if __name__ == '__main__': 
	path = '/Users/youai/client/trunk/galaxywar2.2.6/scripts'
	ext = 'lua'
	try:
		os.remove('ccbiInfo.txt')
	except OSError, e:
		print "no such file but now creating"
	
	findccbi(path,ext)
	print "Done"




