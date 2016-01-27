# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class Tool():
	"""docstring for Tool"""
	removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
	removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
	replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
	replaceTD= re.compile('<td>')
	#把段落开头换为\n加空两格
	replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
	replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
	removeExtraTag = re.compile('<.*?>')
	def replace(self,x):
		x = re.sub(self.removeImg,"",x)
		x = re.sub(self.removeAddr,"",x)
		x = re.sub(self.replaceLine,"\n",x)
		x = re.sub(self.replaceTD,"\t",x)
		x = re.sub(self.replacePara,"\n    ",x)
		x = re.sub(self.replaceBR,"\n",x)
		x = re.sub(self.removeExtraTag,"",x)
		#strip()将前后多余内容删除
		return x.strip()


class BDTB():
	"""docstring for BDTB"""
	def __init__(self,baseUrl,seeLZ,floorTag):
		self.baseUrl = baseUrl
		self.seeLZ = '?see_lz='+str(seeLZ)
		self.tool = Tool()
		self.file = None
		self.floor = 1
		self.defaultTitle = u'百度贴吧'
		self.floorTag = floorTag

		self.user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
		self.headers = { 'User-Agent' : self.user_agent}

	def getPage(self,pageNum):
		try:
			url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
			request = urllib2.Request(url,headers = self.headers)
			response = urllib2.urlopen(request)
			content = response.read()
			return content
		except urllib2.URLError,e:
			if hasattr(e,'code'):
				print e.code
			if hasattr(e,'reason'):
				print e.reason
				return None

	def getTitle(self,page):
		pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
		result = re.search(pattern,page)
		if result:
			print result.group(1).strip()
			return result.group(1).strip()
		else:
			return None

	def getPageNum(self,page):
		pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result = re.search(pattern,page)
		if result:
			print result.group(1).strip()
			return result.group(1).strip()
		else:
			return None

	def getContent(self,page):
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items = re.findall(pattern,page)
		floor = 1
		contents = []
		for item in items:
			content = '\n'+self.tool.replace(item)+'\n'
			contents.append(content.encode('utf-8'))
		return contents

	def setFileTitie(self,title):
		if title is not None:
			self.file = open(title+'.txt','w+')
		else:
			self.file = open(self.defaultTitle + '.txt','w+')

	def writeData(self,contents):
		for item in contents:
			if self.floorTag == '1':
				floorLine = '\n' + str(self.floor) + u'----------------------------------------------------------------------\n'
				self.file.write(floorLine)
			self.file.write(item)
			self.floor += 1

	def start(self):
		indexpage = self.getPage(1)
		pageNum = self.getPageNum(indexpage)
		title = self.getTitle(indexpage)
		self.setFileTitie(title)
		if pageNum == None:
			print 'URL is unvalid,please try again'
			return 
		try:
			print '该帖子总共有' + str(pageNum) + '页'
			for i in range(1,int(pageNum)+1):
				print '正在写入第' + str(i) + '页数据'
				page = self.getPage(i)
				contents = self.getContent(page)
				print contents
				self.writeData(contents)
		except IOError, e:
			print '写入异常,reason'+e.message
		else:
			pass
		finally:
			print '写入任务完成'

print u'请写入帖子代号'
baseUrl = 'http://tieba.baidu.com/p/'+str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input("是否只获取楼主发言，是输入1，否输入0\n")
floorTag = raw_input("是否写入楼层信息，是输入1，否输入0\n")
bdtb = BDTB(baseUrl,seeLZ,floorTag)
bdtb.start()
