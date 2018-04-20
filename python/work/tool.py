#!/usr/python
# coding=utf-8
from tkinter import *
import os,sys,stat,time,datetime,re,json

def get_chinese_path_file_name():
	file_list = []
	cn_list = []
	blank_list = []
	cnpattern = re.compile(u'[\u4e00-\u9fa5]+')
	blankpattern = re.compile(u'\s+')
	# sys.setdefaultencoding('utf-8') 
	def search(path):
		dirs_files = os.listdir(path)
		for file_name in dirs_files:
			full_path = os.path.join(path,file_name)
			full_path = str(full_path) #ascii to unicode
			if cnpattern.search(full_path):
					cn_list.append(full_path)
			if blankpattern.search(full_path):
					blank_list.append(full_path)
			if os.path.isdir(full_path):
				search(full_path)

				

	resPath = p2.get()
	print(len(resPath))
	if len(resPath) == 0:
		r['text'] = "请输入检测文件路径"
		r['background']="red"
		return
	search(resPath)

	cn_list.append("包含中文路径:%d" % len(cn_list))
	blank_list.append("包含空格路径:%d" % len(blank_list))
	file_list = cn_list + blank_list
	r['text'] = '\n'.join(file_list)
	r['background'] = "white"

def check_json_file_format():
	def is_json(path):
		try:
			json.loads(path)
		except ValueError:
			return False
		return True
	file_list = []
	def search(path):
		dirs_files = os.listdir(path)
		for file_name in dirs_files:
			full_path = os.path.join(path,file_name)
			if os.path.isdir(full_path):
				search(full_path)
			else:
				file_ext = file_name.split(".")[-1]
				if file_ext == "json":  
					with open(full_path,'r') as f:
						try:
							jsonStr = f.read()
							if not is_json(jsonStr):
								file_list.append(full_path)
								print("full_path",full_path)
						except Exception as e:
							print(e)
						else:
							pass
						finally:
							pass
						
	jsonPath = p1.get()
	print(len(jsonPath))
	if len(jsonPath) == 0:
		r['text'] = "请输入Json文件路径"
		r['background']="red"
		return
	search(jsonPath)
	file_list.append("总共：%d个错误的json文件" % len(file_list))
	r['text'] = '\n'.join(file_list)
	r['background'] = "white"
root = Tk()
root.wm_title("小公举")



Label(root,text="Json文件路径：").grid(row = 0,sticky = W)
p1 = Entry(root)
p1.grid(row=0,column = 1,sticky = E)

Label(root,text="空格中文路径：").grid(row = 1,sticky = W)
p2 = Entry(root)
p2.grid(row=1,column = 1,sticky = E)

Button(root,text="检测空格中文",command=get_chinese_path_file_name).grid(row=1,column = 2,sticky = W)
Button(root,text="检测Json格式",command = check_json_file_format).grid(row=0,column = 2,sticky = E)

r = Label(root,text = "")
r.grid(row=3,column = 0)


root.mainloop()