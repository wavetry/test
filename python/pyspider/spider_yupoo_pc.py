# _*_ coding: utf-8 _*_
from urllib.request import urlopen
from urllib import request
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
import random,time
import re,sys,socket
import threading

lock = threading.Lock()

BASE_PAGE_URL = "http://x.yupoo.com/photos/xilizhenbiao/albums?tab=gallery&page="
PAGE_URL_LIST =  []
IMG_URL_LIST = []
imgNum =  0
for x in range(1,15):
	PAGE_URL_LIST.append(BASE_PAGE_URL % str(x))
#&tab=max
class Producer(threading.Thread):
	def run(self):
		print('%s Producer is running' % threading.current_thread)
		while len(PAGE_URL_LIST) > 0:
			lock.acquire()
			page_url = PAGE_URL_LIST.pop()
			lock.release()

			response = requests.get(page_url)
			soup = BeautifulSoup(response.content,'lxml')
			# img_list = soup.find_all('img',attrs = {'class':'album__absolute album__img autocover'})
			link_list = soup.find_all('album__main')
			print(link_list)
			for link in link_list:
				print(link['href'])
			lock.acquire()
			# for img in img_list:
			# 	src = img['src']
			# 	if not src.startswith('http'):
			# 		src = 'http:' + src
			# 	IMG_URL_LIST.append(src)
			# lock.release()
			# time.sleep(0.5)


class Consumer(threading.Thread):
	def run(self):
		while True:
			lock.acquire()
			if len(IMG_URL_LIST)  == 0 :
				lock.release()
				continue
			else:
				global imgNum
				imgNum = imgNum + 1
				img_url = IMG_URL_LIST.pop()
				lock.release()
				filename = str(imgNum) + '.jpg'
				path = os.path.join('/Users/youai/Documents/8/',filename)
				print('save %s '  % path)
				urlretrieve(img_url,path)


if __name__ == '__main__':
	for x in range(2):
		Producer().start()

	for x in range(5):
		Consumer().start()




		