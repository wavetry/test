#!/usr/python
# coding=utf-8
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

import os,sys,stat,time,datetime,re,json
result_str=[]
startIndex = 1
fileObject = open('TipConfig.txt', 'wb+')  

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
					r.insert(END,full_path + '\n')
			if blankpattern.search(full_path):
					blank_list.append(full_path)
					r.insert(END,full_path+ '\n')
			if os.path.isdir(full_path):
				search(full_path)

				

	resPath = p2.get()
	print(len(resPath))
	if len(resPath) == 0:
		result['text'] = "请输入检测文件路径"
		result['background']="red"
		return
	r.delete(1.0,END)
	search(resPath)

	file_list = cn_list + blank_list
	result['text'] = ("包含中文路径:%d" % len(cn_list)) + ("包含空格路径:%d" % len(blank_list))
	result['background'] = "white"

def check_all_res_info():
	
	file_list = []
	def search(path):
		dirs_files = os.listdir(path)
		for file_name in dirs_files:
			full_path = os.path.join(path,file_name)
			if os.path.isdir(full_path):
				search(full_path)
			else:
				file_ext = file_name.split(".")[-1]
				if file_ext == "png":
					file_stat = os.stat(full_path)
					size = file_stat [ stat.ST_SIZE ]
					
					temp = str(size/1000) + 'KB\t\t' + full_path + '\n'
					obj = (size,temp)
					file_list.append(obj)
					# r.insert(END,temp)
					# print("full_path",temp)
						
	jsonPath = p1.get()
	print(len(jsonPath))
	if len(jsonPath) == 0:
		result['text'] = "请输入资源文件路径"
		result['background']="red"
		return
	r.delete(1.0,END)
	search(jsonPath)

	file_list.sort(key=lambda student: student[0],reverse=True)
	for k in range(len(file_list)):
		r.insert(END,file_list[k][1])

	result['text'] = "总共：%d个文件" % len(file_list)
	result['background'] = "white"

def replace_all_cn():	
	global startIndex
	startIndex = int(p4.get())
	cnpattern = re.compile(u'[\S]+[\"].[\u4e00-\u9fa5]+.[\"]')
	cnpattern1 = re.compile(u'[\"].[\u4e00-\u9fa5]+.[\"]')
	cnpattern2 = re.compile(u'print\([\"].[\u4e00-\u9fa5]+.[\"]')
	cnpattern3 = re.compile(u'dump\([\S]+[\"].[\u4e00-\u9fa5]+.[\"]')
	cnpattern4 = re.compile(u'--[.]*[\"].[\u4e00-\u9fa5]+.[\"]')


	def replace_ch(target_path):
		global result_str
		global startIndex
		fd = open(target_path,mode='r', encoding='utf-8')
		txt = fd.read()
		# txt = txt.decode("utf-8")
		fd.close()

		# r = u'([一-龥]+)'
		
		result = cnpattern.findall(txt)
		for item in result:
			# print cnpattern2.search(item)
			if cnpattern2.search(item) == None and cnpattern3.search(item) == None and cnpattern4.search(item) == None:
				item1 = cnpattern1.findall(item)[0]
				print (item1)
				txt = txt.replace(item1, "TipConfig[%d]" % startIndex)
				result_str.append("[%d] = %s"  % (startIndex,item1) )
				startIndex = startIndex + 1
				print("startIndex=====>",startIndex)
		# txt = txt.encode('utf-8')

		if len(result_str) > 0:
			newstr = ",\n".join(result_str) + ",\n"
			result_str = []
			newstr = newstr.encode('utf-8')
			fileObject.write(newstr)  
			if None != txt and 0 < txt.__len__():
				fd = open(target_path, 'w')
				fd.write(txt)
				fd.flush()
				fd.close()
			print("".join(result))


	def search(path,ext):
		dirs_files = os.listdir(path)

		for file_name in dirs_files:
			full_path = os.path.join(path,file_name)
			if os.path.isdir(full_path):
				search(full_path,ext)
			file_ext = file_name.split(".")[-1]
			if ext != file_ext:
				continue
			# print(file_name,file_name.find("Config"))
			if file_name.find("Config") == -1:
				replace_ch(full_path)

	root_path = p3.get()
	
	search(root_path,"lua")
	result['text'] = "替换成功"
	result['background'] = "white"

root = Tk()
root.wm_title("小工具")



Label(root,text="资源文件路径：").grid(row = 0,sticky = W)
p1 = Entry(root)
p1.grid(row=0,column = 1,sticky = E)

Label(root,text="空格中文路径：").grid(row = 1,sticky = W)
p2 = Entry(root)
p2.grid(row=1,column = 1,sticky = E)

Label(root,text="替换代码路径：").grid(row = 2,sticky = W)
p3 = Entry(root)
p3.grid(row=2,column = 1,sticky = E)
p4 = Entry(root)
p4.grid(row=2,column = 2,sticky = E)


result = Label(root)
result.grid(row=3,column = 0)

r = Text(root,width=100, height=49)
r.grid(row=4,column = 0,columnspan = 12)


Button(root,text="检测空格中文",command=get_chinese_path_file_name).grid(row=1,column = 2)
Button(root,text="列出资源文件夹下所有图片文件",command = check_all_res_info).grid(row=0,column = 2)
Button(root,text="替换中文",command = replace_all_cn).grid(row=2,column = 3)



# # 滚动文本框
# scrolW = 30 # 设置文本框的长度
# scrolH = 3 # 设置文本框的高度
# scr = scrolledtext.ScrolledText(root, width=scrolW, height=scrolH, wrap=WORD)     # wrap=tk.WORD   这个值表示在行的末尾如果有一个单词跨行，会将该单词放到下一行显示,比如输入hello，he在第一行的行尾,llo在第二行的行首, 这时如果wrap=tk.WORD，则表示会将 hello 这个单词挪到下一行行首显示, wrap默认的值为tk.CHAR
# scr.grid(column=0, columnspan=3)        # columnspan 个人理解是将3列合并成一列   也可以通过 sticky=tk.W  来控制该文本框的对齐方式




root.mainloop()
