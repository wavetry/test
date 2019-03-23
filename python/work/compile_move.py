import os,sys,re,getopt

SRC_PATH = "src\\"
TAR_PATH = "win32\\win32_"

if __name__ == "__main__":
	if os.path.exists("channels.txt"):
		for line in open("channels.txt"):
			os.system("cocos luacompile -s %s -d %s -k 20180309zslm -b 20180309zslm -e --disable-compile" % (SRC_PATH,TAR_PATH + line + "\\src"))
	else:
		print("channels file is not exists")
		
	
