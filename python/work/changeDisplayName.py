#!/usr/bin/env python
# coding=utf-8
import os,re,sys

ext_files = []
ext_strings = []

p = re.compile(r'<key>displayName</key>(\s+)<string>(\S+)</string>(\s+)<key>memberVarAssignmentName</key>(\s+)<string>(\S+)</string>')

def func(m):
	displayName = m.group(2)
	if re.search(r'@@',displayName) == None:
		displayName = m.group(2) + "@@" + m.group(5)
	retult = "<key>displayName</key>%s<string>%s</string>%s<key>memberVarAssignmentName</key>%s<string>%s</string>" % (m.group(1),displayName,m.group(3),m.group(4),m.group(5))
	return retult

def write(path,content):
	with open(path,'w') as f:
		f.write(content)

def changeDisplayName(path,ext):
	dirs_files = os.listdir(path)

	for file_name in dirs_files:
		full_path = os.path.join(path,file_name)
		if os.path.isdir(full_path):
			changeDisplayName(full_path,ext)
		file_ext = file_name.split(".")[-1]
		if ext != file_ext:
			continue

		ext_strings.append(full_path)

		with open(full_path,'r') as f:
			content = p.sub(func,f.read())
			write(full_path,content)

	with open('ccbInfo.txt','a+') as f :
		f.write("\n".join(ext_strings))

if __name__ == '__main__': 
	path = sys.path[0]
	ext = 'ccb'
	try:
		os.remove('ccbInfo.txt')
	except OSError, e:
		print "no such file named ccbInfo.txt but now creating"
	
	changeDisplayName(path,ext)
	print "%d ccb files in all" % len(ext_strings)
	print "Done"














