# _*_ coding:utf-8 _*_
from zipfile import *
import zipfile
import os,re,shutil,json,sys,getopt,datetime,time,base64
from xml.dom.minidom import parse
import xml.dom.minidom

reload(sys)
sys.setdefaultencoding( "utf-8" )

root_path = os.path.split(os.path.abspath(__file__))[0]
root_path = os.popen("cd %s; cd .. ; pwd" % root_path).read().replace("\n", "")
print(root_path)

if __name__ == "__main__":
	argv = sys.argv
	try:
		opts,args = getopt.getopt(argv[1:],'hi:p:',['help','ip=','port='])
	except getopt.GetoptError, err:
		print str(err) 
		sys.exit(2)
	print "opts:", opts

	for o, a in opts:
		if o in ('-r', '--rebuild'):
			rebuild = a == "on"
		elif o in ('-x', '--xxteaPng'):
			xxteaPng = a == "on"
		elif o in ('-x', '--smallPackage'):
			pass
		elif o in ('-o', '--onlyYouaiSDK'):
			onlyYouaiSDK = a == "on"
		elif o in ('-a', '--androidChannel'):
			try:
				tmp = base64.b64decode(a)
				# build_channel_config = json.loads(tmp)
			except:
				pass
		elif o in ('-i', '--iosChannel'):
			pass
		elif o in ('-c', '--customConfig'):
			try:
				custom_config = base64.b64decode(a)
				# if 0 >= custom_config.__len__():
				# 	custom_config = None
				# else:
				# 	custom_config = json.loads(custom_config)
			except:
				pass
		elif o in ('--svnCodeLog', '--svnResLog'):
			log = base64.b64decode(a)
			if None != log:
				# util.write_progress_log(log)
				print(log)
