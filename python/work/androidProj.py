#!/usr/python
# coding=utf-8

import os,sys,shutil,json
oj = os.path.join
oif = os.path.isfile
oid = os.path.isdir

src_channel = "_dafazj"
if __name__ == "__main__":
	try:
		argv = sys.argv
		file_list = argv[1:]
		curPath = os.path.abspath(os.path.dirname(argv[0]))

		tgt_channel = input("新渠道名字：")
		wx_appID = input("微信ID:")
		app_name = input("游戏名字：")

		shutil.copytree(src_channel,"_" + tgt_channel)
	
	os.system("pause")
