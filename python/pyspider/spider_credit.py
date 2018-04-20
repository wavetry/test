#_*_ coding: utf-8 _*_
# coding=utf-8
from urllib.request import urlopen
from urllib import request
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os,random,time
import re,sys,socket
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

lock = threading.Lock()


BASE_PAGE_URL = "https://credit.u51.com"
PAGE_URL = "https://credit.u51.com/youhui/p%s/"
PAGE_URL_LIST = []
IMG_URL_LIST = []
for x in range(1,15):
	PAGE_URL_LIST.append(PAGE_URL % str(x))

driver = webdriver.Chrome()
class Producer(threading.Thread):
	def run(self):
		print('%s Producer is running' % threading.current_thread)
		while len(PAGE_URL_LIST) > 0:
			lock.acquire()
			page_url = PAGE_URL_LIST.pop()
			lock.release()
			print ("page_url",page_url)
			driver.get(page_url)

			soup = BeautifulSoup(driver.page_source,'lxml')
			# print(driver.page_source)
			li_list = soup.find_all('li',class_='clearfix')
			# print (li_list)
			lock.acquire()
			for li in li_list:
				href = li.a['href']
				src = li.a.img['src']
				if not src.startswith('http'):
					src = 'http:' + src
				

				span_list = li.find_all('span')
				bank = span_list[0].a.img['alt']
				IMG_URL_LIST.append((src,bank))
				print(bank)


			lock.release()
			time.sleep(1.5)


class Consumer(threading.Thread):
	def run(self):
		while True:
			lock.acquire()
			if len(IMG_URL_LIST)  == 0 :
				lock.release()
				continue
			else:

				img_url = IMG_URL_LIST.pop()
				lock.release()
				filename = img_url[1] + '.jpg'
				path = os.path.join('/Users/youai/Documents/8/',filename)
				print('save %s '  % path)
				# urlretrieve(img_url[0],path)


if __name__ == '__main__':
	for x in range(1):
		Producer().start()

	for x in range(5):
		Consumer().start()