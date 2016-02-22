# _*_ coding:utf-8 _*_

import urllib
import urllib2
import re
import time
import types
import tool
from bs2 import BeautifulSoup

class Page():
	"""docstring for Page"""
	def __init__(self):
		self.tool = tool.Tool()

	def getCurrentDate(self):
		return time.strftime('%Y-%m-%d',time.localtime(time.time()))

	def getCurrentTime(self):
		return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

	def getPageByUrl(self,url):
		try:
			request = urllib2.Request(url)
			response = urllib2.open(request)
			return response.read().decode('utf-8')
		except urllib2.URLError, e:
			if hasattr(e,'reason'):
				print e.reason
		finally:
			pass






		