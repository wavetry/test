#coding=utf-8
# import urllib
# f = urllib.urlopen('http://www.baidu.com') #read file
# first = f.readline()
# filename = urllib.urlretrieve("http://www.baidu.com",filename='/Users/youai/Documents/2/map/7.html') #save file
# urllib.urlcleanup() # clean cache


#wiki 
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# import datetime
# import random
# from urllib.request import urlretrieve
# pages = set()
# random.seed(datetime.datetime.now())
# # 获取页面所有内链的列表
# def getInternalLinks(bsObj, includeUrl):
# 	internalLinks = []
# 	# 找出所有以"/"开头的链接
# 	for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
# 		if link.attrs['href'] is not None:
# 			if link.attrs['href'] not in internalLinks:
# 				internalLinks.append(link.attrs['href'])
# 	return internalLinks
# # 获取页面所有外链的列表
# def getExternalLinks(bsObj, excludeUrl):
# 	externalLinks = []
# 	# 找出所有以"http"或"www"开头且不包含当前URL的链接
# 	for link in bsObj.findAll("a",
# 		href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
# 		if link.attrs['href'] is not None:
# 			if link.attrs['href'] not in externalLinks:
# 				externalLinks.append(link.attrs['href'])
# 	return externalLinks
# def splitAddress(address):
# 	addressParts = address.replace("http://", "").split("/")
# 	return addressParts
# def getRandomExternalLink(startingPage):
# 	html = urlopen(startingPage)
# 	bsObj = BeautifulSoup(html)
# 	externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
# 	if len(externalLinks) == 0:
# 		internalLinks = getInternalLinks(startingPage)
# 		return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
# 	else:
# 		return externalLinks[random.randint(0, len(externalLinks)-1)]
# def followExternalOnly(startingSite):
# 	externalLink = getRandomExternalLink(startingSite)
# 	print("随机外链是："+externalLink)
# 	try:
# 		urlretrieve(externalLink,filename='/Users/youai/Documents/2/map/'+externalLink+ '.html')
# 	except Exception:
# 		print("error")

	
# 	followExternalOnly(externalLink)
# followExternalOnly("http://www.w3school.com.cn")

# import os
# from urllib.request import urlretrieve
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# downloadDir = "download"
# baseUrl = "http://www.jobbole.com/"

# def getAbsoluteURL(baseUrl,source):
# 	if source.startswith("http://www."):
# 		url = "http://"+source[11:]
# 	elif source.startswith("http://"):
# 		url = source
# 	elif source.startswith("www."):
# 		url = "http://"+source[4:]
# 	else:
# 		url = baseUrl + "/" + source
# 	if baseUrl not in url:
# 		return None
# 	return url

# def getDownloadPath(baseUrl,absoluteUrl,downloadDir):
# 	if absoluteUrl is None:
# 		return ""
# 	path = absoluteUrl.replace("www.","")
# 	path = path.replace(baseUrl,"")
# 	path = downloadDir + path
# 	directory = os.path.dirname(path)

# 	if not os.path.exists(directory):
# 		os.makedirs(directory)

# 	return path

# html = urlopen("http://www.jobbole.com/")
# bsObj = BeautifulSoup(html)
# downloadList = bsObj.findAll(src=True)

# for download in downloadList:
# 	fileUrl = getAbsoluteURL(baseUrl,download["src"])
# 	if fileUrl is not None:
# 		print(fileUrl)
# 		try:
# 			urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDir))
# 		except Exception:
# 			print("error")
# 		else:
# 			pass
# 		finally:
# 			pass

#csv
# import csv

# csvFile = open("../test.csv","w+")
# try:
# 	writer = csv.writer(csvFile)
# 	writer.writerow(('number','number2',"number3"))
# 	for i in range(100):
# 		writer.writerow((i,i+2,i+3))
# finally:
# 	csvFile.close()

# import csv 
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
# bsObj = BeautifulSoup(html)
# table = bsObj.findAll("table",{"class":"wikitable"})[0]
# rows = table.findAll("tr")

# csvFile = open("../editor.csv","wt",newline="",encoding="utf-8")
# writer = csv.writer(csvFile)

# try:
# 	for row in rows:
# 		csvRow = []
# 		for cell in row.findAll(['td','th']):
# 			csvRow.append(cell.get_text())
# 			writer.writerow(csvRow)
# except Exception:
# 	raise
# else:
# 	pass
# finally:
# 	csvFile.close()

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# import string
# def cleanInput(input):
# 	input = re.sub('\n+', " ", input)
# 	input = re.sub('\[[0-9]*\]', "", input)
# 	input = re.sub(' +', " ", input)
# 	input = bytes(input, "UTF-8")
# 	input = input.decode("ascii", "ignore")
# 	cleanInput = []
# 	input = input.split(' ')
# 	for item in input:
# 		item = item.strip(string.punctuation)
# 		if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
# 			cleanInput.append(item)
# 	return cleanInput
# def ngrams(input, n):
# 	input = cleanInput(input)
# 	output = []
# 	for i in range(len(input)-n+1):
# 		output.append(input[i:i+n])
# 	return output

# html = urlopen("http://en.wikipedia.org/wiki/Python_(programing_language)")
# bsObj = BeautifulSoup(html)
# content = bsObj.find("div",{"id":"mw-content-text"}).get_text()
# ngrams = ngrams(content,2)
# print(ngrams)
# print("2-grams count is:"+str(len(ngrams)))	

#概括数据
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# import string
# import operator
# def cleanInput(input):
# 	input = re.sub('\n+', " ", input).lower()
# 	input = re.sub('\[[0-9]*\]', "", input)
# 	input = re.sub(' +', " ", input)
# 	input = bytes(input, "UTF-8")
# 	input = input.decode("ascii", "ignore")
# 	cleanInput = []
# 	input = input.split(' ')
# 	for item in input:
# 		item = item.strip(string.punctuation)
# 		if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
# 			cleanInput.append(item)
# 	return cleanInput
# def ngrams(input, n):
# 	input = cleanInput(input)
# 	output = {}
# 	for i in range(len(input)-n+1):
# 		ngramTemp = " ".join(input[i:i+n])
# 		if ngramTemp not in output:
# 			output[ngramTemp] = 0
# 			output[ngramTemp] += 1
# 	return output
# content = str(
# urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),
# 'utf-8')
# ngrams = ngrams(content, 2)
# sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)
# print(sortedNGrams)	

#马尔科夫连
# from urllib.request import urlopen
# from random import randint
# def wordListSum(wordList):
# 	sum = 0
# 	for word, value in wordList.items():
# 		sum += value
# 	return sum
# def retrieveRandomWord(wordList):
# 	randIndex = randint(1, wordListSum(wordList))
# 	for word, value in wordList.items():
# 		randIndex -= value
# 		if randIndex <= 0:
# 			return word
# def buildWordDict(text):
# 	# 剔除换行符和引号
# 	text = text.replace("\n", " ");
# 	text = text.replace("\"", "");
# 	# 保证每个标点符号都和前面的单词在一起
# 	# 这样不会被剔除，保留在马尔可夫链中
# 	punctuation = [',', '.', ';',':']
# 	for symbol in punctuation:
# 		text = text.replace(symbol, " "+symbol+" ");
# 		words = text.split(" ")
# 		# 过滤空单词
# 		words = [word for word in words if word != ""]
# 		wordDict = {}
# 		for i in range(1, len(words)):
# 			if words[i-1] not in wordDict:
# 				# 为单词新建一个词典
# 				wordDict[words[i-1]] = {}
# 			if words[i] not in wordDict[words[i-1]]:
# 				wordDict[words[i-1]][words[i]] = 0
# 				wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1
# 		return wordDict

# text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
# wordDict = buildWordDict(text)
# # 生成链长为100的马尔可夫链
# length = 100
# chain = ""
# currentWord = "I"
# for i in range(0, length):
# 	chain += currentWord+" "
# 	currentWord = retrieveRandomWord(wordDict[currentWord])
# print(chain)

# import requests 
# params = {'firstname':'Ryan','lastname':'Mitchell'}
# r = requests.post("http://pythonscraping.com/files/processing.php",data = params)
# print(r.text)

# import requests
# from requests.auth import AuthBase
# from requests.auth import HTTPBasicAuth
# auth = HTTPBasicAuth('ryan', 'password')
# r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth=
# auth)
# print(r.text)

import requests
import re
import os
from bs4 import BeautifulSoup

def get_format_filename(input_filename):
	symbol=['?','*','<','>','!']
	for s in symbol:
		while s in input_filename:
			input_filename=input_filename.strip().replace(s,'')
	return input_filename

file_path = "/Users/youai/Documents/3"
headers = {
'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
"Connection":"keep-alive",
"Accept-Encoding": "gzip",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

URL_part1 = "http://r3.gcsit1.website"
URL_part2 = "/pw/thread.php?fid=21"
URL = URL_part1 + URL_part2

start_html = requests.get(URL,headers=headers)
start_html.encoding="utf-8"
bsObj = BeautifulSoup(start_html.text,"html.parser")
print("bsObj",bsObj)

for a in bsObj.find("tbody",{"style":"table-layout:fixed"}).findAll("a"):
	if ("href" in a.attrs) and ("title" not in a.attrs):
		if re.match(r'^htm_data/.+.html',a.attrs['href']):
			a_path = get_format_filename(a.text)
			if not os.path.exists(os.path.join(file_path,a_path)):
				os.makedirs(os.path.join(file_path,a_path))
			os.chdir(file_path+'/'+a_path)
			print(file_path+'/'+a_path)
			f = open(a_path+".txt",'w')
			f.write(a.attrs['href'])










