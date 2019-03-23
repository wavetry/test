#!/usr/python
# coding=utf-8
import os,sys,shutil,json
oj = os.path.join
oif = os.path.isfile
oid = os.path.isdir

if __name__ == "__main__":
	argv = sys.argv
	curPath = os.path.dirname(argv[0])

	with open(os.path.join(curPath,'config.json'),'r',encoding = 'utf-8') as fd:
		config = json.loads(fd.read())
	pathList = os.path.abspath(curPath).split('\\')

	channelName = pathList[-1].split('_')[0]
	print(channelName)
	cocosDir = config["cocosDir"]
	src = oj(curPath,"client\\lua")
	skin_dirs_files = os.listdir(cocosDir)

	for skin_file_name in skin_dirs_files:
		print("skin_file_name",skin_file_name)
		skin_full_path = oj(cocosDir,skin_file_name)
		if os.path.isdir(skin_full_path):
			dirs_files = os.listdir(skin_full_path)
			for file_name in dirs_files:
				full_path = oj(skin_full_path,file_name)
				print("asdasd",file_name[:len(channelName)-1])
				if channelName == file_name[:len(channelName)-1]:
					tgt = oj(full_path,"res\\dataconfig")
					ret = os.popen("Xcopy %s %s /s /e /y" % (src ,tgt )).read()
					print (ret)
						