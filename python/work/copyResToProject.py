#!/usr/python
# coding=utf-8

import multiprocessing
import os,sys,stat,time,datetime

#游戏ccbResources目录
gameDIR = "/Users/youai/newZombie/client/trunk/project/res"

#ccb编辑器ccbResources目录

ccbDIR = "/Users/youai/newZombie/resource/CCB/Published-iOS"
dataDIR = ccbDIR+"/../../data/client"

def copyRes():
	print "拷贝开始"+ str(datetime.datetime.now())
	os.system("rm -rf %s" % gameDIR+"/ccbResources/*")
	os.system("rm -rf %s" % gameDIR+"/ccbi/*")
	os.system("rm -rf %s" % gameDIR+"/data/*")

	def copyTo(srcPath, targetPath):
		os.system("cp -rf %s %s" % (srcPath,targetPath))
		print "%s拷贝到%s结束,时间：%s" % (srcPath,targetPath,str(datetime.datetime.now()))

	p1 = multiprocessing.Process(target = copyTo, args = (ccbDIR+"/ccbResources/*",gameDIR+"/ccbResources/") )
	p1.start()

	p2 = multiprocessing.Process(target = copyTo, args = (ccbDIR+"/ccbi/*",gameDIR+"/ccbi/") )
	p2.start()

	p3 = multiprocessing.Process(target = copyTo, args = (dataDIR+"/*",gameDIR+"/data/") )
	p3.start()

copyRes()