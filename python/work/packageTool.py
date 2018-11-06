#!/usr/python
# coding=utf-8
import os,re,shutil,json,sys,datetime,time,zipfile

from hashlib import md5

# reload(sys)
# sys.setdefaultencoding( "utf-8" )

fd = open("packConfig.json")
config = json.loads(fd.read())
fd.close()

Android_project_path = config["projectPath"]
if not os.path.exists("publish/android/"):
	os.makedirs("publish/android/")

log_fd = open("pack_log.txt",'w+')

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
curPwd = os.getcwd()
for channel in config["channels"]:
	write_log("current channel=========>"+channel)
	pack_path = "../%s/pack/%s/" % (config["branchName"],channel)
	android_poj_path = "%sproj.android_%s/" % (Android_project_path,channel)
	if not os.path.exists(pack_path):
		write_log(pack_path + "is not exists,exit")
		continue
	if not os.path.exists(android_poj_path):
		write_log(android_poj_path + "is not exists,exit")
		continue

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
	# exec_cmd("ant -buildfile build.xml")

	sign_apk = "%sbin/fish-debug.apk" % android_poj_path
	target_apk = "%s/publish/android/%s_%s.apk" % (curPwd,channel, datetime.datetime.now().strftime("%Y%m%d%H%M"))
	# exec_cmd("jarsigner -verbose -keystore %s.keystore -signedjar %s %s %s -storepass 123456"%("signfile/%s" % channel,target_apk,sign_apk,channel))
	exec_cmd("java -jar signfile/signapk.jar signfile/testkey.x509.pem signfile/testkey.pk8 %s %s"% (sign_apk,target_apk))






