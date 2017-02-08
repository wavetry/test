# _*_ coding:utf-8 _*_

import urllib
import urllib2
import re

class spider(object):
	"""docstring for spider"""
	def __init__(self,baseUrl):
		self.user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
		self.headers = { 'User-Agent' : self.user_agent}
		self.baseUrl = baseUrl

	def getPage(self,pageId):
		try:
			url = self.baseUrl + str(pageId)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			content = response.read()
			#print content
			return content
		except urllib2.URLError, e:
			if hasattr(e,'reason'):
				print e.reason
			if hasattr(e,'code'):
				print e.code
			return None
		finally:
			pass
	
	def getPageId(self,content):
		pattern = re.compile('<h3>(.*?)</h3>')
		result = re.search(pattern,content)
		pattern = re.compile('(\d+)')
		result = re.search(pattern,result.group(1).strip())
		if result:
			print result.group(1).strip()
			return result.group(1).strip()
		else:
			return None

	def start(self):
		pageContent = self.getPage('')
		pageId = self.getPageId(pageContent)
		while pageId != None:
			pageContent = self.getPage(pageId)
			pageId = self.getPageId(pageContent)
		print pageId

spd = spider('http://www.heibanke.com/lesson/crawler_ex00/')
spd.start()	

# # _*_ coding:utf-8 _*_

# from urllib import  urlencode
# import urllib2
# import re
# class posting(object):
# 	"""docstring for posting"""
# 	def getResult(self,login_data):
# 		try:
# 			url = 'http://www.heibanke.com/lesson/crawler_ex02/'
# 			req = urllib2.Request(url)
# 			req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# 			req.add_header('Origin','www.heibanke.com')
# 			response = urllib2.urlopen(req,data = login_data.encode('utf-8'))
# 			print (response.read())
# 			return response.read()
# 		finally:
# 			pass
# 	def start(self):
# 		psd = input('password:')
# 		while psd != 'q':
# 			user = 'linzhilang'
# 			token = 'QiIMeJckdnGs3LRKAwrCHuMYJSJ5KrdS'
# 			login_data = urlencode([
# 				('csrfmiddlewaretoken',token),
# 				('username',user),
# 				('password',psd),
# 				('pagerefer','http://www.heibanke.com?csrfmiddlewaretoken=token&username=user&password=psd')
# 				])
# 			content = self.getResult(login_data)
# 			pattern = re.compile('<h3>(.*?)</h3>')
# 			result = re.search(pattern,content)
# 			if result:
# 				print result.group(1).strip()
# 			psd= input('password:')

# ps = posting()
# ps.start()
