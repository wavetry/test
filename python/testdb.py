#!/usr/python
# coding=utf-8
import datetime, time, os, sys, datetime, json, thread, base64, re, hashlib, MySQLdb
import cookielib, urllib, urllib2
import multiprocessing

import os,sys,stat,time,datetime,re,json
the_conn_str = {}
the_conn_str["HOST"] 	= "10.21.210.120"
the_conn_str['USER'] 	= "root"
the_conn_str['PASSWORD'] = "mongo123123"
the_conn_str['PORT'] 	= 3306
the_conn_str['NAME'] 	= "galaxy"

def update_server_ver_num(ver_num):
	conn = MySQLdb.connect(host=the_conn_str['HOST'],user=the_conn_str['USER'],passwd=the_conn_str['PASSWORD'], port=the_conn_str['PORT'], db=the_conn_str['NAME'],charset='utf8') 
	conn.autocommit(True)
	cursor = conn.cursor()
	update_sql = "UPDATE `upgrade` SET ver_num=%s" % ver_num
	cursor.execute(update_sql)
	conn.close()


	cookiejar = cookielib.CookieJar()
	urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
	values = {'username':"root", 'passowrd':"123456" }
	data = urllib.urlencode(values)
	request = urllib2.Request("http://10.21.210.120:8001/login", data)
	url = urlOpener.open(request)
	url.read()

	for cookie in cookiejar:
		print cookie

	url = urlOpener.open('http://10.21.210.120:8001/upgrade/make')
update_server_ver_num(0.01)