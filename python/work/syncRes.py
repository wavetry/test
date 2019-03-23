#!/usr/python
# coding=utf-8

#同步皮肤资源工具
import os,sys,getopt,shutil,json

# reload(sys)
# sys.setdefaultencoding( "gbk" )

oj = os.path.join
oif = os.path.isfile
oid = os.path.isdir

def isListContain(lists,obj):
	for o in lists:
		if obj == o:
			return True
	return False

#打包成exe路径问题好多坑 直接用脚本绝对路径
if __name__ == "__main__":
	try:
		argv = sys.argv
		file_list = argv[1:]
		curPath = os.path.abspath(os.path.dirname(argv[0]))	
		print("curPath======>",curPath)
		print("file_list",file_list)
		if len(file_list) == 0:
			print("空的文件列表")
		else:
			with open(oj(curPath,'config.json') , 'r', encoding='utf-8') as fd:
				config = json.loads(fd.read())

			TortoisePath = config["Tortoise"]
			dirs_files = os.listdir(curPath)

			for file_name in dirs_files:
				full_path = oj(curPath,file_name)
				print("file_name",file_name,full_path)
				if os.path.isdir(full_path):
					for file_path in file_list:
						suffixPath = file_path[len(curPath):]
						partition = suffixPath[1:].find("\\")
						print("partition",partition)
						suffixPath = suffixPath[partition+1:]
						tgt = (full_path+suffixPath)
						print("已复制到",len(curPath),suffixPath,tgt)
						ret = os.popen("copy %s %s /Y" % (file_path ,tgt )).read()
			os.popen("\"%s\"/command:commit /path:%s /notempfile /closeonend:0" % (TortoisePath,curPath))
	except Exception as e:
		with open("error.log", "w+") as f:
			f.write(str(sys.exc_info()))	
			f.write(str(e))
		print(sys.exc_info())
		
		print("Exception",e)
		inp_exit = input("input to exit")
	
	os.system("pause")
	

