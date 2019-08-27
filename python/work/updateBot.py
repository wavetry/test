#!/usr/python
# -*- coding: utf-8 -*-
import os,sys
import telegram
import sys   
reload(sys)   
sys.setdefaultencoding('utf-8')  

bot = telegram.Bot(token='800541044:AAHqNWCRXDoSiKLEAeR2wEDpnXRTX8fxEEg') # 替换为实际的 token

# chat_id = '-394436373'
chat_id = '-315458430'
insert = raw_input("更新描述：".encode("gbk"))
# os.popen("packer_tool.exe")
pack_name = ""
with open ("updata_info.txt") as f:
	pack_name = f.read()
# 发送简单文本消息
if insert != "":
	bot.send_message(chat_id=chat_id, text= "更新包：%s\n更新内容:%s" % (pack_name,insert) )  # 替换为实际的频道 ID(英文唯一标识)	


# # 发送带标题网址链接
# bot.send_message(chat_id=chat_id,
#     text='<a href="http://slowread.net/monitor-hostloc/">HOSTLOC 交易贴提醒</a>.', 
#     parse_mode=telegram.ParseMode.HTML)

# # 其它文字样式
# bot.send_message(chat_id=chat_id, text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.', parse_mode=telegram.ParseMode.HTML)
