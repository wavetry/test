#-*- coding:utf-8 -*-

__author__ = '打补丁的狮子'

import sys
import os
from datetime import datetime

def myDirList():
    currpath = os.path.abspath('.')
    print("————————————%s————————————" % currpath)
    for f in os.listdir(currpath):
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        if os.path.isdir(f):
            #flag = '<dir>' if os.path.isdir(f) else ''
            #print('%10d %s   %5s   %s' % (fsize, mtime, flag, f))
            print('%10d %s   <dir>   %s' % (fsize, mtime, f))
        elif os.path.isfile(f):
        	print('%10d %s   <file>   %s' % (fsize, mtime, f))

if(__name__ == "__main__"):
    if 0==len(sys.argv):
        print("")
    elif 1 <=len(sys.argv):
        if '-l' == sys.argv[1].lower():
            myDirList()
        elif '-?' == sys.argv[1].lower() or '-h' == sys.argv[1].lower():
            print("            -l            显示目录列表")
            print("            -?/-h         显示帮助信息")
        else:
            print("无效的参数，请输入-？或-h参数来获取帮助信息！")