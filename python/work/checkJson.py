#!/usr/python
# coding=utf-8
import json,os, json, sys, getopt
file_list = []
def is_json(path):
	try:
		json.loads(path)
	except ValueError:
		return False
	return True

def search(path):
	dirs_files = os.listdir(path)
	for file_name in dirs_files:
		full_path = os.path.join(path,file_name)
		full_path = unicode(full_path) #ascii to unicode
		if os.path.isdir(full_path):
			search(full_path)
		else:
			file_ext = file_name.split(".")[-1]
			if file_ext == "json":  
				with open(full_path,'r') as f:
					jsonStr = f.read()
					if not is_json(jsonStr):
						file_list.append(full_path)


if __name__ == '__main__':
	try:
		reload(sys)
		sys.setdefaultencoding('utf-8')
		root_path = raw_input('input json file path:')
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
			search(root_path)

		for obj in file_list:
			print obj
		raw_input('Press Enter to exit...')
	except:
		print "Unexpected error:", sys.exc_info() # sys.exc_info()返回出错信息
		raw_input('press enter key to exit') #这儿放一个等待输入是为了不让程序退出
	