#!/usr/python
# coding=utf-8

import os,sys,shutil,json

oj = os.path.join
oif = os.path.isfile
oid = os.path.isdir

if __name__ == "__main__":
	argv = sys.argv
	curPath = os.path.abspath(os.path.dirname(argv[0]))	
	win32Path = oj(curPath,"..\\") 
	dirs_files = os.listdir(win32Path)

	for file_name in dirs_files:
		
		file_path = oj(win32Path,file_name)
		print(file_name,oid(file_path),file_name.find("%d"))
		if oid(file_path) and file_name.find("%d") > 0:
			src = oj(curPath,"cocosstudio")
			tgt = oj(file_path,"cocosstudio")
			ret = os.popen("Xcopy %s %s /s /e /y" % (src ,tgt )).read()
			print("ret",src,tgt,ret)
			src = oj(curPath,"res")
			tgt = oj(file_path,"res")
			ret = os.popen("Xcopy %s %s /s /e /y" % (src ,tgt )).read()
			print("ret",src,tgt,ret)