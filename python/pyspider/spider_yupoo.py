# -*- coding: utf-8 -*- 
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
import random,time
import re,sys

class spider():
	"""docstring for spider"""
	def __init__(self):
		self.dirs = ""
		self.img_nums = 0
		self.site_head = 'http://v.yupoo.com'
		self.user_agent_list = [
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
			"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
		]

		self.iplist = []
		html = self.request_url("http://haoip.cc/tiqu.htm")
		iplistn = re.findall(r'r/>(.*?)<b',html,re.S)
		for ip in iplistn:
			i = re.sub('\n','',ip)
			self.iplist.append(i.strip())

		

	def request_url(self,url):
		UA = random.choice(self.user_agent_list)
		req = request.Request(url)
		req.add_header('User-Agent',UA)
		res = ""
		try:
			with request.urlopen(req) as f:
				print('Status:',f.status,f.reason)
				if f.status == 200:
					res = f.read().decode('utf-8')
				else:
					return ""
		except Exception:
			print("error",url)
		return res
		


	# def request_url(self,url):
	# 	res = ""
	# 	try:
	# 		res = urlopen(url)
	# 	except Exception:
	# 		print("error",url)
	# 	return res

	def html(self,href):
		html = self.request_url(href)
		if html == "":
			print("html is empty string")
			return
		html_bsObj = BeautifulSoup(html)

		imgs = html_bsObj.find('table',class_='DayView').find_all('img')
		index = 0
		print("len of imgs",len(imgs))
		for img in imgs:
			img_url = img['src']
			print(img_url)
			index = index + 1
			self.img_nums = self.img_nums + 1
			self.save(img_url,index)

		print("图片总数：",self.img_nums)

	def img(self,pageUrl):
		img_html = self.request_url(pageUrl)
		img_bsObj = BeautifulSoup(img_html)
		tg = img_bsObj.find('div',class_='main-image')
		if tg is not None:
			img_url = tg.find('img')['src']
			self.save(img_url)

	def save(self,img_url,index):
		name= str(index)
		path = self.dirs+name+".jpg"
		isExists = os.path.exists(os.path.join(path))
		if not isExists:
			urlretrieve(img_url,path)
			return True
		else:
			return False
		

	def mkdir(self,path,txt):
		path = path.strip()
		isExists = os.path.exists(os.path.join("/Users/youai/Documents/3",path))
		if not isExists:
			os.makedirs(os.path.join("/Users/youai/Documents/3",path))
		os.chdir(os.path.join("/Users/youai/Documents/3",path))
		with open('desc.txt','w') as f:
			f.write(txt)

	def all_url(self,url,start_page=0):
		start_html = self.request_url(url)
		bsObj = BeautifulSoup(start_html)
		a_list = bsObj.findAll('a',class_='Seta')
		index = 0
		print("总页数：",len(a_list))
		for a in a_list:
			title = a.get_text()
			title = re.sub('/',' ',title)
			index = index + 1
			title = str(index) + '_' + title
			href = self.site_head + a['href'] + "?style=story"
			
			# print(href)
			self.mkdir(title[0:250],a.get_text())
			if index > int(start_page):
				self.html(href)
			time.sleep(random.random())
			print("page:",index)

targetUrl = "http://v.yupoo.com/photos/xilizhenbiao/albums/"
sp = spider()
sp.all_url(targetUrl,sys.argv[1])

		
