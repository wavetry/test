# -*- coding:utf-8 -*-
import re
import scrapy #导入scrapy包
from bs4 import BeautifulSoup
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from dingdian.items import DingdianItem ##这是我定义的需要保存的字段，（导入dingdian项目中，items文件中的DingdianItem类）
class Myspider(scrapy.Spider):
	name = 'dingdian'
	allowed_domain = ['23us.com']
	base_url = 'http://www.23us.com/class/'
	bashurl = '.html'

	def start_requests(self):
		for i in range(1,11):
			url = self.base_url + str(i) + '_1' + self.bashurl
			yield Request(url,self.parse)

	def parse(self,response):
		print(response.text)