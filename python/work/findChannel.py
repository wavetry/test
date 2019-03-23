#!/usr/python
# coding=utf-8
import os,sys,shutil,json
oj = os.path.join
oif = os.path.isfile
oid = os.path.isdir

if __name__ == "__main__":
	argv = sys.argv
	curPath = os.path.dirname(argv[0])
	channel = input("输入查询渠道:")

	skin_dirs_files = os.listdir("%s/.." % curPath)
	for skin_file_name in skin_dirs_files:
		skin_full_path = oj(cocosDir,skin_file_name)
		if os.path.isdir(skin_full_path):
			dirs_files = os.listdir(skin_full_path)
			for file_name in dirs_files:
				full_path = oj(skin_full_path,file_name)
				if channel == file_name:
					print(skin_file_name)