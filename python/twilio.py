#coding: utf-8

import socket
import time
from sms import sms
import logging
import time
from twilio.rest import Client


def sms(t):
    account_sid = " "

    auth_token = " "

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="= ",#自己的手要号码 
        from_=" ",#在网站上申请的手机码，只能用这个号码发信息
        body=t.decode("utf-8"))#编码密码使用utf-8才发送中文。

    print(message.sid)


def port_try(host,port):
    shijian=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((host,port))
        t=host+"服务器 "+str(port)+" 连接正常 "+str(shijian)
        #sms(t)
        print t
    except Exception:
        w=host+" 服务器 "+str(port)+" 无法连接 "+str(shijian)
        print w
        sms(w)
    sk.close()

file = open("/root/script/ip.txt")#ip地址写法192.16.0.1:80

while True:
    line = file.readline().strip('\n')
    if len(line)==0:break
    ip=str(line.split(':',1)[0])
    port=int(line.split(':',1)[1])
    port_try(ip,port)
    time.sleep(2)