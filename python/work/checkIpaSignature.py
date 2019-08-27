#!/usr/python
# -*- coding: utf-8 -*-
import time,os
# import telegram
import sys   
reload(sys)   
sys.setdefaultencoding('utf-8')  
# bot = telegram.Bot(token='800541044:AAHqNWCRXDoSiKLEAeR2wEDpnXRTX8fxEEg') # 替换为实际的 token

chat_id = '-394436373'
# chat_id = '-315458430'
curPath = os.getcwd()

def checkSignature():
	dirs_files = os.listdir(curPath)
	for file_name in dirs_files:
		file_ext = os.path.splitext(file_name)[1]
		if file_ext == ".ipa":
			real_file_name = os.path.basename(file_name).split('.')[0]
			ret = os.popen("ideviceinstaller %s" % file_name).read()
			print("checkSignature====",real_file_name,ret)
			if ret.find('error') > 0:
				text= u"%s %s 掉签了".encode("gbk") % (time.strftime('%Y-%m-%d %X',time.localtime()),real_file_name)
				print(text)
				# bot.send_message(chat_id=chat_id, text= text.decode('gbk') )
				os.popen('curl -X POST "https://api.telegram.org/bot800541044:AAHqNWCRXDoSiKLEAeR2wEDpnXRTX8fxEEg/sendMessage" -d "chat_id=%s&text=%s"' % (chat_id,text))

def timer(n):  
	while True:    
		print(time.strftime('%Y-%m-%d %X',time.localtime()))    
		checkSignature()  # 此处为要执行的任务    
		time.sleep(n)


if __name__ == '__main__':
	timer(60*60)
