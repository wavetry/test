#!/usr/python
# coding=utf-8
import csv,os,sys
logDict = {}

if __name__ == "__main__":
	argv = sys.argv
	file_list = argv[1:]
	if len(file_list) == 0:
		print("no input log file")
	else:
		with open(file_list[0],'r') as f:
			logList = f.readlines()
			with open('filterLog.csv','w') as csvf:

				for i in range(0,len(logList)):
					index = logList[i].find("client error")
					error_log = logList[i][index:]
					
					if logDict.get(error_log) == None:
						logDict[error_log] = 0
						# print error_log
					logDict[error_log] = logDict[error_log] + 1

				writer = csv.writer(csvf)
				for key,value in logDict.items():
					temp = [key,value]
					writer.writerow(temp)

	os.popen('filterLog.csv')

