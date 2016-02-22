# _*_ coding:utf-8 _*_

import urllib
import urllib2
import re
import time
import types
import page
import mysql
import sys
from bs4 import BeautifulSoup

class Spider():
	"""docstring for Spider"""
	def __init__(self):
		self.page_num = 1
		self.total_num = None
		self.page_spider = page.Page()
		self.mysql = mysql.Mysql()

	def getCurrentTime(self):
		return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

	def getCurrentDate(self):
		return time.strftime('%Y-%m-%d',time.localtime(time.time()))




		