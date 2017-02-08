#!/usr/bin/python
#coding=utf-8

#SMTP email insterting
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import re

import smtplib

addresses = []
toaddresses = []
p = re.compile(r'\d+')

def addimg(src,imgid):
	fp = open(src,'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	msgImage.add_header('Content-ID',imgid)
	return msgImage

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'zuihaochaye@163.com'
password = '12345abcde'
to_addr = "15989193326@163.com"
smtp_server = "smtp.163.com"

msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
# msg = MIMEMultipart('related') 
# with open('content.html','r') as f:
# 	content = f.read()

# msgText = MIMEText(content,'html', 'utf-8')

# msg.attach(msgText)
# att = MIMEText(open('/Users/youai/develop/git/python/sprite.png', 'rb').read(), 'base64', 'utf-8')
# att["Content-Type"] = 'application/octet-stream'
# att["Content-Disposition"] = 'attachment; filename="1.jpg"'
# msg.attach(att)


msg['From'] = _format_addr('me <%s>' % from_addr)
msg['To'] = _format_addr('ssss <%s>' % to_addr)
msg['Subject'] = Header('hello', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)

server.sendmail(from_addr, [to_addr], msg.as_string())
# with open('mail.txt','r') as f:
# 	numbers = p.findall(f.read())
# 	for n in numbers:
# 		addr = str(n) + '@qq.com'
# 		addresses.append(addr)
# 		msg['To'] = _format_addr('—— <%s>' % addr)
# 		# print("msg msg ",addr)
# 		# server.sendmail(from_addr, addresses, msg.as_string())
# 		addresses = []
	

server.quit()