#!/usr/python
# coding=utf-8
import os,sys,re,getopt
def get_chinese_path_file_name(respath):
	file_list = []
	cn_list = []
	blank_list = []

	cnpattern = re.compile(u'[\u4e00-\u9fa5]+')
	blankpattern = re.compile(u'\s+')
	def search(path):
		dirs_files = os.listdir(path)
		for file_name in dirs_files:
			full_path = os.path.join(path,file_name)
			full_path = unicode(full_path) #ascii to unicode
			if cnpattern.search(full_path):
					cn_list.append(full_path)
			if blankpattern.search(full_path):
					blank_list.append(full_path)
			if os.path.isdir(full_path):
				search(full_path)

	search(respath)

	cn_list.append("包含中文路径:%d" % len(cn_list))
	blank_list.append("包含空格路径:%d" % len(blank_list))
	file_list = cn_list + blank_list
	for obj in file_list:
			print obj

if __name__ == '__main__':
	try:
		reload(sys)
		sys.setdefaultencoding('utf-8')
		root_path = raw_input('输入资源路径:')
		root_path = unicode(root_path) #ascii to unicode

		# windows
		# root_path = root_path.replace('/','\\')
		#linux
		root_path = root_path[:-1]

		argv = sys.argv
		try:
			opts, args = getopt.getopt(argv[1:], 'hvp:', ['path='])
		except getopt.GetoptError, err:
			print str(err) 
			sys.exit(2)
		for o, a in opts:
			if o in ('-p', '--path'):
				root_path = a
		# print file_list
		if None != root_path:
			get_chinese_path_file_name(root_path)

		
		raw_input('Press Enter to exit...')
	except:
		print "Unexpected error:", sys.exc_info() # sys.exc_info()返回出错信息
		raw_input('press enter key to exit') #这儿放一个等待输入是为了不让程序退出