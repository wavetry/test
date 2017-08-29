# coding: utf-8
from urllib.request import urlopen
from urllib import request
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os,signal
import random,time
import re,sys,socket
import threading

lock = threading.Lock()
BASE_PAGE_URL = "http://slide.astro.sina.com.cn/gif/"
PAGE_URL_LIST =  []
IMG_URL_LIST = []

response = requests.get(BASE_PAGE_URL)
soup = BeautifulSoup(response.content,'lxml')

p = re.compile(r'img=\S+\.gif')

img_list = soup.find_all('img')
print(response.content)
for img in img_list:
	src = img['src']
	print(src)
	match = p.search(src)
	print("match",match)
	if match:
		print (match.group())