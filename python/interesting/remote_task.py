# coding:utf-8

import smtplib
import poplib
import email
#SMTP email insterting
from email.header import decode_header,Header
from email.utils import parseaddr, formataddr
from email import encoders
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import re
import os,sys,string
import time
import base64

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

"""
此函数用来重置邮箱里面的内容，如果不重置，下次打开程序就会立即获取邮箱里面的命令（关机）
"""
def Reset():
    from_addr = 'zuihaochaye@163.com'
    password = '12345abcde'
    to_addr = "zuihaochaye@sina.com"
    smtp_server = "smtp.163.com"

    msg = MIMEText('<html><body><h1>Hello</h1>' +
        '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
        '</body></html>', 'html', 'utf-8')
    msg['From'] = _format_addr('client <%s>' % from_addr)
    msg['To'] = _format_addr('server <%s>' % to_addr)
    msg['Subject'] = Header('reset', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)

    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

"""
用POP3来读取远程邮箱内容作为命令
"""
while True:
    host='pop.sina.com'
    duyoujian=poplib.POP3(host)
    duyoujian.user('zuihaochaye@sina.com')
    duyoujian.pass_('zuihaochaye')
    total=duyoujian.stat()

    str=duyoujian.top(total[0],0)
    # print str 
    strr=[]
    for x in str[1]:
        try:
            strr.append(x.decode())
        except:
            try:
                strr.append(x.decode('gbk'))
            except:
                strr.append(x.decode('big5'))
    msg=email.message_from_string('\n'.join(strr))
    Titt=decode_header(msg['subject'])
# 	 content=decode_header(msg[''])
    # print Titt

    if Titt[0][1]:
        ttle=Titt[0][0].decode(Titt[0][1])
    else:
        ttle=Titt[0][0]
    print ttle
    if ttle=='ls':
        Reset()
        os.system('ls -a')
        
        # os.system('shutdown -s -t 60')
        
        