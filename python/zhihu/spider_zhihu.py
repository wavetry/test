# _*_ coding:utf-8 _*_
import requests
import urllib
import re
import random
from time import sleep
def main():
	url = 'https://www.zhihu.com/question/22591304/followers'
	user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
	headers = { 'User-Agent' : user_agent}
	i = 1
	for x in xrange(20,360,20):
		data = {
		'start':'0',
		'offset':str(x),
		'_xsrf':'a128464ef225a69348cef94c38f4e428'
		}
		content=requests.post(url,headers=headers,data=data,timeout=10).text
		content = '<img src="https://pic4.zhimg.com/e5d922d1c13cd7755bc05c65db45196b_m.jpg" class="zm-item-img-avatar">'
		imgs=re.findall('<img src=\"(.*?).jpg',content) 
		print (content)
		print (imgs)
		for img in imgs:
			try:
				img = img.replace('\\','')
				pic=img+'.jpg'
				path='/Users/youai/Documents/2/map/' + str(i)+'.jpg'
				urllib.urlretrieve(pic,path)
				i+=1
				sleep(random.uniform(0.5,1))
				print(u'downloading pic')
			except :
				print (u'miss one pic')
			else:
				pass
			finally:
				pass
	
if __name__ == '__main__':
	main()