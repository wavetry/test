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
		a_list = bsObj.find('div',class_='all').findAll('a')
		for a in a_list:
			title = a.get_text()
			print(title)
			self.mkdir(title)
			self.html(a['href'])

targetUrl = "http://www.mzitu.com/all"
sp = spider()
sp.all_url(targetUrl)

# for a in a_list:
# 	title = a.get_text()
# 	path = str(title).strip()
# 	# if os.path.isdir(os.path.join("/Users/youai/Documents/1",path)):
# 	# 	os.remove(os.path.join("/Users/youai/Documents/1",path))
# 	os.makedirs(os.path.join("/Users/youai/Documents/1",path))
# 	# os.chdir("/Users/youai/Documents/1/"+path)
# 	dirs = "/Users/youai/Documents/1/"+path
# 	href = a['href']

# 	html = request_url(href)
# 	html_bsObj = BeautifulSoup(html)
# 	max_span = html_bsObj.findAll('span')[10].get_text()

# 	for page in range(1,int(max_span) + 1):
# 		page_url = href + '/' + str(page)
# 		img_html = request_url(page_url)
# 		img_bsObj = BeautifulSoup(img_html)
# 		tg = img_bsObj.find('div',class_='main-image')
# 		if tg is not None:
# 			img_url = tg.find('img')['src']
# 			name=  img_url[-9:-4]
# 			# img = request_url(img_url)
# 			urlretrieve(img_url,dirs+"/"+name+".jpg")
# 			print(img_url)
		
