#!/usr/bin/env python
# coding=utf-8
import os,re,sys

p = re.compile(r'DataStrings\[\S+\]')

def func(m):
	name = m.group(1)
	retult = "MangoShare.getTranslate(%s)" % m.group(1)
	print("func",name,result)
	return retult

def write(path,content):
	with open(path,'w') as f:
		f.write(content)

def translate(path,ext):
	dirs_files = os.listdir(path)

	for file_name in dirs_files:
		full_path = os.path.join(path,file_name)
		if os.path.isdir(full_path):
			translate(full_path,ext)
		file_ext = file_name.split(".")[-1]
		if ext != file_ext:
			continue

		ext_strings.append(full_path)

		with open(full_path,'r') as f:
			content = p.sub(func,f.read())
			write(full_path,content)

	with open('luaInfo.txt','a+') as f :
		f.write("\n".join(ext_strings))

if __name__ == '__main__': 
	path = sys.path[0]
	ext = 'lua'
	try:
		os.remove('luaInfo.txt')
	except OSError, e:
		print "no such file named luaInfo.txt but now creating"
	
	translate(path,ext)
	print "%d lua files in all" % len(ext_strings)
	print "Done"