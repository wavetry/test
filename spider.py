# _*_ coding:utf-8
import urllib
import urllib2
import re
import time

class QSBK():
	"""spider class"""
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
		self.headers = { 'User-Agent' : self.user_agent}
		self.stories = []
		self.enable = False
	def getPage(self,pageIndex):
		try:
			url = "http://www.qiushibaike.com/hot/page/" + str(pageIndex)
			request = urllib2.Request(url,headers = self.headers)
			response = urllib2.urlopen(request)
			content = response.read().decode('utf-8')
			return content
		except urllib2.URLError,e:
			if hasattr(e,'code'):
				print e.code
			if hasattr(e,'readon'):
				print e.reason
				return None

	def getPageItems(self,pageIndex):
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print '页面加载失败'
			return None
		pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?<h2>(.*?)</h2>.*?<div.*?'+
                        'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
		items = re.findall(pattern,pageCode)
		pageStories = []
		for item in items:
			haveImg = re.search('img',item[3])
			if not haveImg:
				replaceBR = re.compile('<br>')
				text = re.sub(replaceBR,'\n',item[1])
				pageStories.append([item[0].strip(),text.strip(),item[2].strip(),item[4].strip()])
		return pageStories

	def loadPage(self):
		if self.enable == True:
			if len(self.stories) < 3:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex +=1

	def getOneStory(self,pageStories,page):
		for story in pageStories:
			input = raw_input()
			self.loadPage()
			if input == "q":
				self.enable = False
				return 
			print u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s" %(page,story[0],story[2],story[3],story[1])

	def start(self):
		print u"正在读取糗事百科,按回车查看新段子，q退出"
		self.enable = True
		self.loadPage()
		nowpage = 0
		while self.enable:
			if len(self.stories)>0:
				pageStories = self.stories[0]
				nowpage+=1
				del self.stories[0]
				self.getOneStory(pageStories,nowpage)

spider = QSBK()
spider.start()
