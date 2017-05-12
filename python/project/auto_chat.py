#coding=utf8
import requests
import itchat,time
from itchat.content import *

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key'	: KEY,
		'info'	: msg,
		'userid': '=_=',
	}
	try:
		r = requests.post(apiUrl,data = data).json()
		return r.get('text')
	except:
		return 
@itchat.msg_register([ MAP, CARD, NOTE, SHARING])
def text_reply(msg):
	msg.user.send('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
	msg.download(msg.fileName)
	typeSymbol = {
		PICTURE: 'img',
		VIDEO: 'vid', }.get(msg.type, 'fil')
	return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friends(msg):
	msg.user.verify()
	msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT,isGroupChat=True)
def group_reply(msg):
	defaultReply = 'I receive: ' + msg['Text']
	reply = get_response(msg['Text'])
	return reply or defaultReply

@itchat.msg_register(TEXT)
def tuling_reply(msg):
	defaultReply = 'I receive: ' + msg['Text']
	reply = get_response(msg['Text'])
	return reply or defaultReply
itchat.auto_login(hotReload = True)
msg = u'发给%s的消息'
# myself = itchat.get_friends(update = True)[0] #myself
# itchat.send(msg % (myself['DisplayName'] or myself['NickName']),myself['UserName'])

man  = itchat.search_friends(name=u'勇初')[0]
print(man)

for index in range(1):
	man.send('hello this is test msg')
	time.sleep(1)
itchat.run()






