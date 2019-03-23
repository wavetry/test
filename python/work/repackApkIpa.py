#!/usr/python
# coding=utf-8

#同步通用配置工具
import os,sys,getopt,shutil,json,datetime,time,zipfile

# reload(sys)
# sys.setdefaultencoding( "gbk" )

oj = os.path.join
oif = os.path.isfile
oid = os.path.isdir


#打包成exe路径问题好多坑 直接用脚本绝对路径
if __name__ == "__main__":
	try:
		argv = sys.argv
		exe_path = os.path.dirname(argv[0])
		file_list = argv[1:]
		
		for file_path in file_list:
			file_name = os.path.basename(file_path)
			file_dir = os.path.dirname(file_path)
			file_ext = file_name.split(".")[-1]
			new_file_name = file_name.split(".")[-2] + ".zip"
			# print("file_path",file_path,file_ext,new_file_name)
			if file_ext == "apk":
				print("当前打的包:",file_name)
				new_file_path = oj(file_dir,new_file_name)
				invite_code = input("请输入邀请码:")
				shutil.copyfile(file_path,new_file_path)
				z = zipfile.ZipFile(new_file_path, 'r')
				z.extractall(path=oj(file_dir, "temp"))
				z.close()

				# print("file_dir===>",oj(file_dir, "temp"))
				os.chdir(file_dir)
				with open("temp/assets/invite_code.txt",'w') as f:
					f.write(invite_code)
				shutil.rmtree('temp/META-INF')

				new_zip_name = "%s_%s" % (file_name.split(".")[-2],invite_code)
				shutil.make_archive(new_zip_name,'zip',"temp")
				shutil.move(new_zip_name + '.zip',new_zip_name + '.apk')
				shutil.rmtree(oj(file_dir, "temp"))
				os.remove(new_file_path)
				print("打包成功===============>",new_zip_name + '.apk')
			elif file_ext == "ipa":
				print("当前打的包:",file_name)
				new_file_path = oj(file_dir,new_file_name)
				invite_code = input("请输入邀请码:")
				shutil.copyfile(file_path,new_file_path)
				z = zipfile.ZipFile(new_file_path, 'r')
				z.extractall(path=oj(file_dir, "temp"))
				z.close()
				os.chdir(file_dir)

				with open("temp/Payload/game iOS.app/invite_code.txt",'w') as f:
					f.write(invite_code)
				new_zip_name = "%s_%s" % (file_name.split(".")[-2],invite_code)
				shutil.make_archive(new_zip_name,'zip',"temp")
				shutil.move(new_zip_name + '.zip',new_zip_name + '.ipa')
				shutil.rmtree(oj(file_dir, "temp"))
				os.remove(new_file_path)
				print("打包成功===============>",new_zip_name + '.ipa')


	except Exception as e:
		print(sys.exc_info())
		print("Exception",e)
		inp_exit = input("input to exit")
		
	os.system("pause")

