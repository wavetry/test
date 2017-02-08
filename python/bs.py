# from bs4 import BeautifulSoup
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

# bsObj = BeautifulSoup(html)
# print(bsObj.prettify())
# print(bsObj.name)
# bsObj.contents
# bsObj.p.children
# bsObj.descendants
# .next_elements 
# .previous_elements

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os

#http://scozjb.com/thread0806.php?fid=15
class spider():
	"""docstring for spider"""
	def __init__(self):
		self.dirs = ""
	
	def request_url(self,url):
		res = ""
		try:
			res = urlopen(url)
		except Exception:
			print("error",url)
		return res

	def html(self,href):
		html = self.request_url(href)
		html_bsObj = BeautifulSoup(html)
		max_span = html_bsObj.findAll('span')[10].get_text()
		print("max_span",max_span)
		for page in range(1,int(max_span)+1):
			page_url = href + '/' + str(page)
			self.img(page_url)

	def img(self,pageUrl):
		img_html = self.request_url(pageUrl)
		img_bsObj = BeautifulSoup(img_html)
		tg = img_bsObj.find('div',class_='main-image')
		if tg is not None:
			img_url = tg.find('img')['src']
			self.save(img_url)

	def save(self,img_url):
		name=  img_url[-9:-4]
		urlretrieve(img_url,self.dirs+name+".jpg")

	def mkdir(self,path):
		path = path.strip()
		isExists = os.path.exists(os.path.join("/Users/youai/Documents/3",path))
		if not isExists:
			os.makedirs(os.path.join("/Users/youai/Documents/3",path))
			return True
		else:
			return False
		os.chdir(os.path.join("/Users/youai/Documents/3",path))

	def all_url(self,url):
		start_html = self.request_url(url)
		bsObj = BeautifulSoup(start_html)
		a_list = bsObj.findAll('a')
		for a in a_list:
			title = a.get_text()
			print(title)
			print(a['href'])
			# self.mkdir(title)
			# self.html(a['href'])

targetUrl = "http://scozjb.com/thread0806.php?fid=15"
sp = spider()
sp.all_url(targetUrl)

		

