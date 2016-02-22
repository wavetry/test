# _*_ coding:utf-8 _*_

import MySQLdb
import time
class Mysql():
	#获取当前时间
	def getCurrentTime(self):
		return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

	"""docstring for Mysql"""
	def __init__(self):
		try:
			self.db = MySQLdb.connect('ip','username','password','db_name')
			self.cur = self.db.cursor()
		except MySQLdb.Error, e:
			print self.getCurrentTime(),"连接数据库错误，原因%d: %s" % (e.args[0], e.args[1])
		
		finally:
			pass
		