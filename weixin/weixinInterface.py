# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json
import urllib, urllib2
import re
import cookielib
import time
import xml.dom.minidom
import json
import sys
import math
import json


from lxml import etree

DEBUG = False

MAX_GROUP_NUM = 35 # 每组人数

QRImagePath = '/qrcode.jpg'

tip = 0
uuid = ''

base_uri = ''
redirect_uri = ''

skey = ''
wxsid = ''
wxuin = ''
pass_ticket = ''
deviceId = 'e000000000000000'

BaseRequest = {}

ContactList = []
My = []

def getUUID():
    global uuid
    
    url = 'https://login.weixin.qq.com/jslogin'
    params = {
              'appid': 'wx782c26e4c19acffb',
              'fun': 'new',
              'lang': 'zh_CN',
              '_': int(time.time()),
              }
    
    request = urllib2.Request(url = url, data = urllib.urlencode(params))
    response = urllib2.urlopen(request)
    data = response.read()
    
    # print data
    
    # window.QRLogin.code = 200; window.QRLogin.uuid = "oZwt_bFfRg==";
    regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)"'
    pm = re.search(regx, data)
    
    code = pm.group(1)
    uuid = pm.group(2)
    
    if code == '200':
        return True
    
    return False


def showQRImage():
    global tip
    url = 'https://login.weixin.qq.com/qrcode/' + uuid
    params = {
        't': 'webwx',
        '_': int(time.time()),
    }

    request = urllib2.Request(url = url, data = urllib.urlencode(params))
    response = urllib2.urlopen(request)

    tip = 1
    #f = open(QRImagePath, 'wb')
    #f.write(response.read())
    #f.close()
    return 'fail'

def youdao(word):
    qword = urllib2.quote(word)
    baseurl = r'http://fanyi.youdao.com/openapi.do?keyfrom=ouyongchu&key=2012217765&type=data&doctype=json&version=1.1&q='
    url = baseurl+qword
    resp = urllib2.urlopen(url)
    fanyi = json.loads(resp.read())
    if fanyi['errorCode'] == 0:        
        if 'basic' in fanyi.keys():
            trans = u'%s:\n%s\n%s\n网络释义：\n%s'%(fanyi['query'],''.join(fanyi['translation']),' '.join(fanyi['basic']['explains']),''.join(fanyi['web'][0]['value']))
            return trans
        else:
            trans =u'%s:\n基本翻译:%s\n'%(fanyi['query'],''.join(fanyi['translation']))        
            return trans
    elif fanyi['errorCode'] == 20:
        return u'对不起，要翻译的文本过长'
    elif fanyi['errorCode'] == 30:
        return u'对不起，无法进行有效的翻译'
    elif fanyi['errorCode'] == 40:
        return u'对不起，不支持的语言类型'
    else:
        return u'对不起，您输入的单词%s无法翻译,请检查拼写'% word
    

class WeixinInterface:
 
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
 
    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="ouyongchu" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法        
 
        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr

    def POST(self):        
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        content=xml.find("Content").text#获得用户所输入的内容
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        
        if getUUID() == False:
            r = showQRImage()
            time.sleep(1)
    
            return self.render.reply_text(fromUser,toUser,int(time.time()),u"测试,您的uuid是："+r)
       
        
        if type(content).__name__ == "unicode":
            content = content.encode('UTF-8')
        Nword = youdao(content)
        if content == "林智浪":
            Nword = "林智浪怎么这么帅呢?"
        return self.render.reply_text(fromUser,toUser,int(time.time()),Nword)
