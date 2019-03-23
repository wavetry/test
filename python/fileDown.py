#!/usr/bin/python
#encoding:utf-8
import urllib
def sfinds(start_str,end,html):
	start=html.find(start_str)
	ifstart==0:
		start+=len(start_str)
		end=html.find(end,start)
	if end==0:
	return html[start:end].strip()

def getHtml(url):
	p=urllib.urlopen(url)
	html=p.read()
	return html

def getImg(html):
	reg=rurl[^]*[^u]*[^r]*[^l]*[^]*/url
	imgae=re.compile(reg)
	imglist=re.findall(imgae,str(html))
	return imglist