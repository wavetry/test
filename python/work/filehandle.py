#!/usr/python
# coding=utf-8

import os,sys,json,getopt,shutil,time

oj = os.path.join
oif = os.path.isfile
oid = os.path.isdir

def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def search(path):
	dirs_file = os.listdir(path)

	for file_name in dirs_file:
		full_path = oj(path,file_name)
		if oid(full_path):
			search(full_path)
		# file_ext = file_name.split('.')[-1]
		print(file_name,TimeStampToTime(os.path.getmtime(full_path)))

if __name__ == "__main__":
	argv = sys.argv
	curPath = os.path.abspath(os.path.dirname(argv[0]))

	search(curPath)
		
	os.system("pause")