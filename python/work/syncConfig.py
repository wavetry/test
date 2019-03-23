#!/usr/python
# coding=utf-8

#同步通用配置工具
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
		print("file_list",file_list)

		PathB = os.path.abspath(os.path.dirname(argv[0]))
		PathA = oj(PathB,"..\\..\\") 
		print("PathB,PathA",PathB,PathA)

		with open(oj(PathB,'config.json') , 'r', encoding='utf-8') as fd:
			config = json.loads(fd.read())


		copyDir = config["copyDir"]
		filterSuffix = config["filterSuffix"]
		filterChannel = config["filterChannel"]
		luaDir = config["luaDir"]
		luaFilterSuffix = config["luaFilterSuffix"]
		luaFilterChannel = config["luaFilterChannel"]

		
		dirs_files = os.listdir(PathA)

		for file_name in dirs_files:
			Type = file_name[-2:] #ZJ YS
			print("Type",file_name)
			if isListContain(filterSuffix,Type) == False and isListContain(filterChannel,file_name) == False:
				full_path = oj(PathA,file_name)

				#only copy certain files
				if len(file_list) > 0:
					for file_path in file_list:
						suffixPath = file_path[len(PathB):]
						# print ("suffixPath",full_path,suffixPath)
						tgt = (full_path+suffixPath)
						print("已复制到",tgt)
						ret = os.popen("copy %s %s /Y" % (file_path ,tgt )).read()
				#copy all
				else:
					for directory in copyDir:
						src = oj(PathB,directory)
						tgt = oj(full_path,directory)
						print("src",src,tgt)
						ret = os.popen("Xcopy %s %s  /s /e /y" % (src ,tgt )).read()
						print (ret)
				
		
		dirs_files = os.listdir(luaDir)
		#copy lua config
		src = oj(PathB,"client\\lua")

		for file_name in dirs_files:
			full_path = oj(luaDir,file_name)
			if os.path.isdir(full_path):
				Type = file_name[-2:] #zj ys
				print("lua Type",file_name)
				if isListContain(luaFilterSuffix,Type) == False and isListContain(luaFilterChannel,file_name) == False:
					
					if len(file_list) > 0:
						for file_path in file_list:
							file_name = os.path.basename(file_path)
							if file_name[-4:] == ".lua":
								tgtDir = oj(full_path,"res\\dataconfig")
								tgt = oj(tgtDir , file_name)
								# print ("file_name",tgt,tgtDir,file_name)
								ret = os.popen("copy %s %s /Y" % (file_path ,tgt )).read()
								print("已复制到",tgt)
					else:
						tgt = oj(full_path,"res\\dataconfig")
						ret = os.popen("Xcopy %s %s /s /e /y" % (src ,tgt )).read()
						print (ret)
						
	except Exception as e:
		with open("error.log", "w+") as f:
			f.write(str(sys.exc_info()))	
			f.write(str(e))
		print(sys.exc_info())
		
		print("Exception",e)
		inp_exit = input("input to exit")
	
	os.system("pause")

