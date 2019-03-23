#!/usr/python
# coding=utf-8
import os,shutil,sys,getopt
file_list = []

def movefile(srcfile,dstfile):
	if not os.path.isfile(srcfile):
		print("%s not exist!" % srcfile)
	else:
		fpath,fname=os.path.split(dstfile)    #分离文件名和路径
		if not os.path.exists(fpath):
			os.makedirs(fpath)                #创建路径
		shutil.move(srcfile,dstfile)          #移动文件
		print "move %s -> %s"%( srcfile,dstfile)

def copyfile(srcfile,dstfile):
	if not os.path.isfile(srcfile):
		print "%s not exist!"%(srcfile)
	else:
		fpath,fname=os.path.split(dstfile)    #分离文件名和路径
		if not os.path.exists(fpath):
			os.makedirs(fpath)                #创建路径
		shutil.copyfile(srcfile,dstfile)      #复制文件
		print "copy %s -> %s"%( srcfile,dstfile)

def search(path,dstfile):
	dirs_files = os.listdir(path)
	for file_name in dirs_files:
		full_path = os.path.join(path,file_name)
		full_path = unicode(full_path) #ascii to unicode
		if os.path.isdir(full_path):
			search(full_path)
		else:
			file_ext = file_name.split(".")[-1]
			if file_ext == "luac":  
				# dstfile = ""
				# copyfile(full_path,dstfile)
				file_list.append(full_path)
				# print(full_path)

if __name__ == '__main__':
	try:
		reload(sys)
		sys.setdefaultencoding('utf-8')
		# root_path = raw_input('input file path:')
		# root_path = unicode(root_path) #ascii to unicode

		
		root_path = "" #src path
		dst_path = ""
		argv = sys.argv
		try:
			opts, args = getopt.getopt(argv[1:], 'sd:', ['srcph=','dstph='])
		except getopt.GetoptError, err:
			print str(err) 
			sys.exit(2)
		for o, a in opts:
			if o in ('-s', '--srcph'):
				root_path = a
			if o in ('-d', '--dstph'):
				dst_path = a
		print root_path
		print dst_path
		if None != root_path:
			# search(root_path)
			shutil.rmtree(dst_path)
			os.mkdir(dst_path)
			shutil.copytree(root_path, dst_path)

		# for obj in file_list:
		# 	print obj
		raw_input('Press Enter to exit...')
	except:
		print "Unexpected error:", sys.exc_info() # sys.exc_info()返回出错信息
		raw_input('press enter key to exit') #这儿放一个等待输入是为了不让程序退出
	