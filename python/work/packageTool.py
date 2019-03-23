#!/usr/python
# -*- coding: utf-8 -*-
import os,re,shutil,json,sys,datetime,time

reload(sys)
sys.setdefaultencoding( "gbk" )
fd = open("config.json")
config = json.loads(fd.read())
fd.close()

if not os.path.exists("publish/android/"):
	os.makedirs("publish/android/")

log_fd = open("pack_log.txt",'w+')
subgame_back_path = "../%s/pack/subgame/" % config["branchName"]
curPwd = os.getcwd()
aapt_path = "%s/aapt.exe" % curPwd
android_jar_path = "%s/android.jar" % curPwd
Android_project_path = config["projectPath"]
channel_config_path = "../%s/channel_config.txt" % config["branchName"]
channel_createMd5_path = "../createMd5/channel_config.json"
encrypt_exe_path = "../%s/encrypt.exe" % config["branchName"]

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

def move_subgame(channel,filterList):
	target_path = "../%s/pack/%s/res/subgame/" % (config["branchName"],channel)
	dirs_files = os.listdir(subgame_back_path)
	for file_name in dirs_files:
		if file_name not in filterList:
			if os.path.exists(os.path.join(target_path,file_name)):
				shutil.rmtree(os.path.join(target_path,file_name))
			shutil.copytree(os.path.join(subgame_back_path,file_name),os.path.join(target_path,file_name))
		else:
			src_path = "../%s/pack/%s/src/app/subgame/" % (config["branchName"],channel)
			shutil.rmtree(os.path.join(src_path,file_name))
exec_cmd("svn up ../%s" % config["branchName"] )
###############1 配置文件
with open(channel_config_path,"w+") as f:
	for channel in config["channels"]:
		f.write(channel + '\n')
shutil.copyfile("config.json",channel_createMd5_path)

###############2 筛选不要的子游戏
os.chdir("../%s" % config["branchName"])
for channel in config["channels"]:
	if channel != "juhao":
		subgamePath = "win32/%s/res/subgame/"
		if os.path.exists(subgamePath):
			shutil.rmtree(subgamePath)

###############3加密资源代码
os.chdir("../%s" % config["branchName"])

start=time.clock()
exec_cmd("encrypt.exe")
write_log("encrypt cost time:" + str(time.clock() - start))
os.chdir(curPwd)

##聚豪子游戏资源备份

if os.path.exists(subgame_back_path):
	shutil.rmtree(subgame_back_path)
shutil.move("../%s/pack/juhao/res/subgame/" % config["branchName"],subgame_back_path)
############### 筛选不要的子游戏
for channel in config["channels"]:
	if config["filterSubgame"][channel] != None:
		move_subgame(channel,config["filterSubgame"][channel])

# ###############4 生成md5
os.chdir(curPwd)
nowtime = time.clock()
exec_cmd( "..\createMd5\\rungame.bat" )
write_log("createMd5 cost time:" + str(time.clock() - nowtime))
nowtime = time.clock()
##############5打包 暂时安卓
for channel in config["channels"]:
	write_log("current channel=========>"+channel)
	pack_path = "../%s/pack/%s/" % (config["branchName"],channel)
	android_poj_path = "%sproj.android_%s/" % (Android_project_path,channel)
	print(pack_path,android_poj_path)
	
	if not os.path.exists(android_poj_path):
		write_log(android_poj_path + "is not exists,exit")
		continue

	if not os.path.exists(pack_path):
		write_log(pack_path + "is not exists,exit")
		continue
	shutil.rmtree(android_poj_path + "bin")
	res_path = android_poj_path + "assets/res"
	src_path = android_poj_path + "assets/src"
	if os.path.exists(res_path):
		shutil.rmtree(res_path)
	if os.path.exists(src_path):
		shutil.rmtree(src_path)

	print(res_path,src_path)
	shutil.copytree(pack_path + "res",res_path)
	shutil.copytree(pack_path + "src",src_path)
	os.chdir(android_poj_path)
	exec_cmd("ant -buildfile build.xml")

	sign_apk = "%sbin/fish-debug.apk" % android_poj_path
	target_apk = "%s/publish/android/%s_%s.apk" % (curPwd,channel, datetime.datetime.now().strftime("%Y%m%d%H%M"))
	unsigned_apk = "%s/publish/android/%s_%s_unsigned.apk" % (curPwd,channel, datetime.datetime.now().strftime("%Y%m%d%H%M"))
	# exec_cmd("jarsigner -verbose -keystore %s.keystore -signedjar %s %s %s -storepass 123456 -digestalg SHA1 -sigalg MD5withRSA"%("signfile/%s" % channel,target_apk,sign_apk,channel))
	# exec_cmd("java -jar signfile/signapk.jar signfile/testkey.x509.pem signfile/testkey.pk8 %s %s"% (sign_apk,target_apk))
	# shutil.copy(sign_apk,target_apk)
	# 打包资源
	string = u"聚豪游戏".encode("gbk")
	print(string)
	exec_cmd("%s package -f -M AndroidManifest.xml -S res -A assets -I %s -F bin/resources" % (aapt_path,android_jar_path))
	exec_cmd("java -cp %s/sdklib.jar com.android.sdklib.build.ApkBuilderMain %s -v -u -z bin/resources -f bin/classes.dex -rf src" % (curPwd,unsigned_apk))
	exec_cmd("jarsigner -verbose -keystore signfile/%s_keystore -signedjar %s %s %s -storepass %s123456 -digestalg SHA1 -sigalg MD5withRSA"%(channel,target_apk,unsigned_apk,string,channel))
	exec_cmd("jarsigner -verify %s" % target_apk)

############6签名
exec_cmd("echo sign")
write_log("package cost time:" + str(time.clock() - nowtime))
