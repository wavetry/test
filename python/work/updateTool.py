#!/usr/python
# coding=utf-8
import os,re,shutil,json,sys,datetime,time,zipfile

from hashlib import md5
# reload(sys)
# sys.setdefaultencoding( "utf-8" )

fd = open("config.json")
config = json.loads(fd.read())
fd.close()

channel_config_path = "../%s/channel_config.txt" % config["branchName"]
channel_packDiff_path = "../packDiff/channel_config.txt"
channel_createMd5_path = "../createMd5/channel_config.json"
encrypt_exe_path = "../%s/encrypt.exe" % config["branchName"]
create_md5_path = "../createMd5/changeMd5/"
pre_update_path = "../../client/"
log_fd = open("log.txt","w+")

def exec_cmd(cmd_str):
	print(cmd_str)
	log_fd.write(cmd_str)
	log_fd.write("\n")
	log_fd.flush()
	ret = os.popen(cmd_str).read()
	print(ret)
	log_fd.write(ret)
	log_fd.flush()

def write_log(log_str):
	print(log_str)
	log_fd.write(log_str)
	log_fd.write("\n")
	log_fd.flush()
exec_cmd("svn up ../%s" % config["branchName"] )
###############1
with open(channel_config_path,"w+") as f:
	for channel in config["channels"]:
		f.write(channel + '\n')

with open(channel_packDiff_path,"w+") as f:
	for channel in config["channels"]:
		f.write(channel + '\n')

shutil.copyfile("config.json",channel_createMd5_path)

###############2
curPwd = os.getcwd()
os.chdir("../%s" % config["branchName"])

start=time.clock()
exec_cmd("encrypt.exe")
write_log("encrypt cost time:" + str(time.clock() - start))
os.chdir(curPwd)

##############3 生成差异json文件 

nowtime = time.clock()
exec_cmd( "..\createMd5\\rungame.bat" )
write_log("createMd5 cost time:" + str(time.clock() - nowtime))

for channel in config["channels"]:
	write_log( "current channel=====>" + channel )
	pack_path = "../%s/pack/%s/" % (config["branchName"],channel)

	# pack_res_path = pack_path + "res"
	# md5_res_path = create_md5_path + "res"

	# startTime = time.clock()
	# if os.path.exists(md5_res_path):
	# 	shutil.rmtree(md5_res_path)
	# shutil.copytree(pack_res_path, md5_res_path)

	# pack_src_path = pack_path + "src"
	# md5_src_path = create_md5_path + "src"
	# if os.path.exists(md5_src_path):
	# 	shutil.rmtree(md5_src_path)
	# shutil.copytree(pack_src_path, md5_src_path)

	# write_log("copy file cost time:" + str(time.clock() - startTime))

	
	pack_diff_channel_path = "../packDiff/channel/%s/" % channel

	if not os.path.exists(pack_diff_channel_path):
		os.mkdir(pack_diff_channel_path)
	shutil.copyfile(pack_path + "md5Config.lua",pack_diff_channel_path + "Smd5Config.lua")


#get file's md5
def md5_file(name):
	m = md5()
	a_file = open(name,'rb')
	m.update(a_file.read())
	a_file.close()
	return m.hexdigest()

#get channel newest zip file
def get_newest_zipfile(path):
	dirs_files = os.listdir(path)
	max_time = 0

	for file_name in dirs_files:
		time = re.findall('(\d+)',file_name)
		file_ext = file_name.split(".")[-1]
		if file_ext == "zip" and max_time < time:
			newest_file = os.path.join(path,file_name)
			max_time = time
	return newest_file

def create_diff_files():
	nowtime = time.clock()
	for channel in config["channels"]:
		channel_path = "%s/%s_app/" % (pre_update_path,channel)
		newest_file = get_newest_zipfile(channel_path)
		write_log(channel + " newest_file "+newest_file)
		# shutil.unpack_archive(newest_file)
		z = zipfile.ZipFile(newest_file, 'r')
		z.extractall(path=channel_path + "temp")
		z.close()

		pack_diff_channel_path = "../packDiff/channel/%s/" % channel
		if not os.path.exists(pack_diff_channel_path):
			os.mkdir(pack_diff_channel_path)
		shutil.copyfile(channel_path + "temp/md5Config.lua",pack_diff_channel_path + "Lmd5Config.lua")

	exec_cmd( "..\packDiff\\rungame.bat" )
	write_log("create_diff_files cost time:" + str(time.clock() - nowtime))

def pack_diff():
	
	for channel in config["channels"]:
		channel_path = "%s/%s_app/" % (pre_update_path,channel)
		pack_path = "../%s/pack/%s/" % (config["branchName"],channel)
		pack_diff_channel_path = "../packDiff/channel/%s/" % channel
		pack_diff_files_path = pack_path + "diff/"
		if not os.path.exists(pack_diff_files_path):
			os.mkdir(pack_diff_files_path)

		with open(pack_diff_files_path + "version.lua",'w') as f:
			with open(channel_path + "temp/version.lua",'r') as fa:
				ver = float(fa.read())
				f.write(str(ver + 0.1))

		with open(pack_diff_channel_path + "diffFiles.json") as f:
			diffList = json.loads(f.read())
			for value in diffList:
				temp = os.path.dirname(value['KEY'])
				temp_full_path = os.path.join(pack_diff_files_path,temp)
				# print (temp)
				if not os.path.exists(temp_full_path):
					os.makedirs(temp_full_path)
				# if os.path.basename(value['KEY']) != "md5Config.json":
				shutil.copyfile(os.path.join(pack_path,value['KEY']),os.path.join(pack_diff_files_path,value['KEY']))
		time = datetime.datetime.now().strftime("%Y%m%d%H%M")
		file_name = "%s%s-app_%s" % (channel_path,channel,time)
		shutil.make_archive(file_name,'zip',pack_diff_files_path)
		shutil.rmtree(channel_path + "temp")
		shutil.rmtree(pack_diff_files_path)



		with open(file_name + ".md5","w") as f:
			f.write(md5_file(file_name + ".zip"))
		# exec_cmd("svn add %s.zip" % file_name)
		# exec_cmd("svn add %s.md5" % file_name)
		# os.chdir(channel_path)
		# exec_cmd("svn commit  -m  \"autocommit diff package by updateTool\"")
if __name__ == '__main__':
	argv = sys.argv
	create_diff_files()

	nowtime = time.clock()
	pack_diff()
	write_log("pack_diff cost time:" + str(time.clock() - nowtime))

	write_log("total cost time:" + str(time.clock() - start))
	write_log("pack diff files finished!!!")
	log_fd.close()
	