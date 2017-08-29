# _*_ coding:utf-8 _*_

import urllib
import threading
from bs4 import BeautifulSoup
import requests
import os
import time
from urllib.request import urlretrieve
FACE_URL_LIST = []

PAGE_URL_LIST = []

BASE_PAGE_URL = "https://www.doutula.com/photo/list/?page="

for x in range(1,800):
	url = BASE_PAGE_URL + str(x)
	PAGE_URL_LIST.append(url)

print("PAGE_URL_LIST len",len(PAGE_URL_LIST))
glock = threading.Lock()

class Producer(threading.Thread):
	def run(self):
		print('%s Producer is running' % threading.current_thread)
		while len(PAGE_URL_LIST) > 0:
			glock.acquire()
			page_url = PAGE_URL_LIST.pop()
			glock.release()

			response = requests.get(page_url)
			soup = BeautifulSoup(response.content,'lxml')
			img_list = soup.find_all('img',attrs={'class':'img-responsive lazy image_dta'})
			glock.acquire()

			for img in img_list:
				src = img['data-original']
				if not src.startswith('http'):
					src = 'http:' + src

				FACE_URL_LIST.append(src)
			glock.release()
			time.sleep(0.5)


class Consumer(threading.Thread):
	def run(self):
		print ('%s Consumer is running' % threading.current_thread)
		while True:
			glock.acquire()
			if len(FACE_URL_LIST) == 0:
				glock.release()
				continue 
			else:
				face_url =  FACE_URL_LIST.pop()
				glock.release()
				filename = face_url.split('/')[-1]
				path = os.path.join('/Users/youai/Documents/6/',filename)
				print('save %s' % path)
				urlretrieve(face_url,filename=path)

if __name__ == '__main__':
	for x in range(2):
		Producer().start()

	for x in range(5):
		Consumer().start()

		