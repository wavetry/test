# !/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#io
# name = input("input your name: ")
# print("name:",name)
# if name == "handsome":
# 	print("handsome")
# else:
# 	print("ugly")

#list
# classmate = [1,2,3]
# classmate.append(4)
# classmate.insert(0,0)
# classmate.pop()
# print(classmate)

#tuple
# t = (1,2,3,[5,7])
# print(t[3][1])

#loop
# for v in (range(1010)):
# 	print(v)
# n = 100
# while n>0:
# 	print(n)
# 	n=n-1

#dictionary
# dictionary = {'Aba':123123123,'Bob':1231231231,"Coc":123123123}
# print('Aba' in dictionary)
# print(dictionary.pop('Aba'))
# print(dictionary.get('Aba',-1))

#set
# s = set([12,5,45])
# print(s)
# s.remove(12)
# s.add(45)
# d = set([2,4,5])
# print(s&d)

#
######
# from testpy import fa
# from testpy import calc
# from testpy import person
# print(calc())
# print(calc(1,2))
# print(calc(*[1,2,3]))
# person('Adam', 45, gender='M', job='Engineer')
# person('a',34,**{'gender':2})

# from testpy import man
# man('Adam',age = 45)

# from testpy import fact
# from testpy import factx
# n = int(input("number:"))
# print(fact(n))
# print(factx(n))

# from testpy import moveF
# move(16,'A','B','C')

# from testpy import fbnc
# n=int(input("number:"))
# print(fbnc(n))

#切片
# ls = [1,2,3,4,]
# print(ls[:3:2])
# print("sadad"[::-1])

#访问字典或者列表
# dic = {'a':1,'b':2,'c':3}
# ls = {1,2,3,4}
# for k in dic:
# 	print(k)
# print('\n')

# for v in dic.values():
# 	print(v)
# print('\n')

# for k,v in dic.items():
# 	print(k,v)

# from collections import Iterable
# a = isinstance('asd',Iterable)
# print(a,'\n')

# for i,value in enumerate(ls):
# 	print(i,value)

#列表生成式
# ls = [x*x for x in range(10) if x%2==1]
# ls = [x*y for x in range(10) if x%2==1 for y in range(10) if x%2==1]
# import os
# ls = [d for d in os.listdir('.')]
# L1 = ['Hello', 'World', 18, 'Apple', None]
# ls = [s.lower() for s in L1 if isinstance(s,str)]

#九九乘法表
# ls = [str(x) + ' x ' + str(y) + '=' + str(x*y) for x in range(1,10) for y in range(1,10)]
# print(ls)
# g = [x*x for x in range(10)]
# for x in g:
# 	print(x)

# def fib(max):
# 	n,a,b = 0,0,1
# 	while n < max:
# 		yield b
# 		a,b = b,a + b
# 		n = n + 1
# 	return 'done'
# g = fib(6)
# while True:
# 	try:
# 		x = next(g)
# 		print('g:',x)
# 	except StopIteration as e:
# 		print("return value:",e.value)
# 		break

#map and reduce
# def mt(n):
# 	return n * n
# print(list(map(mt,[1,2,3])))

# from functools import reduce
# def fn(x,y):
# 	return x *10+y
# print(reduce(fn,[1,2,3,4,5,5,6,4,1]))	

# from functools import reduce
# def prod(L):
# 	def mysum(x,y):
# 		return x*y
# 	return reduce(mysum,L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# from testpy import str2float
# from testpy import primes

# import sys
# sys.path.append('')

# class Student(object):
# 	"""docstring for Student"""
# 	__slots__ = ('name','__age','set_age')
# 	def __init__(self, name,age):
# 		super(Student, self).__init__()
# 		self.name = name
# 		self.__age = age

# 	def print_info(self):
# 		print(self.name,self._age)

# s = Student('Adult',12)
# def set_age(self,age):
# 	self.age = age
# from types import MethodType
# s.set_age = MethodType(set_age,s)
# s.set_age(15)
# s.age = 116
# s.n = 12
# print(s.age)


#文件读写 'r'read 'rb'read in binary 'w'write 'wb'write in binary
# with open('test.lua','r',encoding = 'gbk',errors = 'ignore') as f:
# 	print(f.read(100))
# 	# for lines in f.readlines():
# 	# 	print(lines.strip())

# with open('test.txt','w',encoding = 'utf-8')as f:
# 	f.write('Hello Woarld')

# #StringIO BytesIO
# from io import StringIO
# f = StringIO('linzhilang\n')
# f.write('linzhilang')
# print(f.getvalue())

#序列化
# import pickle
# l = [1,2,3]
# p =  pickle.dumps(l)
# f = open('dump.txt','wb')
# pickle.dump(l,f)
# f.close()
# print(p)
# f=open('dump.txt','rb')
# l = pickle.load(f)
# f.close()
# print(l)

		
#json
# import json
# d=dict(name='lzl',age=2)
# r=json.dumps(d)
# lr=json.loads(r)
# print(type(r))
# print(type(lr))

# import json

# class Student(object):
# 	def __init__(self, name, age, score):
# 		self.name = name
# 		self.age = age
# 		self.score = score
	
# def student2dict(std):
# 		return {
# 	    	'name': std.name,
# 	    	'age': std.age,
# 	    	'score': std.score
# 	    	}
# s = Student('Bob', 20, 88)
# print(json.dumps(s, default=student2dict))

# print(json.dumps(s, default=lambda s: s.__dict__))


# from datetime import datetime
# now = datetime.now()
# print(now)
# dt = datetime(1024,2,3,2,2)
# print(dt)

# from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# from urllib import request

# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))


# from urllib import request, parse

# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])

# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# def log(func):
# 	def wrapper(*args,**kw):
# 		print('call %s():' % func)
# 		return func(*args,**kw)
# 	return wrapper

# # @log
# def now():
# 	print("linzhilang")
# now = log(now)
# now()

#decorator
# import functools

# def log(func):
# 	@functools.wraps(func)
# 	def wrapper(*args,**kw):
# 		print('call %s ():' % func.__name__)
# 		return func(*args,**kw)
# 	return wrapper

# def logg(text):
# 	def decorator(func):
# 		@functools.wraps(func)
# 		def wrapper(*args,**kw):
# 			print('%s %s ():' % (text,func.__name__))
# 			r = func(*args,**kw)
# 			print('end call')
# 			return r
# 		return wrapper
# 	return decorator

# @log
# def now():
# 	print("now")
# now()

#@property
# class Screen(object):
# 	"""docstring for Screen"""
# 	@property
# 	def width(self):
# 	    return self._width
# 	@width.setter
# 	def width(self, value):
# 	    self._width = value
# 	@property
# 	def height(self):
# 	    return self._height
# 	@height.setter
# 	def height(self, value):
# 	    self._height = value

# 	@property
# 	def resolution(self):
# 	    return self._height*self._width
	
# 	def __init__(self):
# 		super(Screen, self).__init__()

		
# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.resolution)
# assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return 'Student object (name=%s)' % self.name
#     __repr__ = __str__

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b

#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration();
#         return self.a # 返回下一个值
#     def __getitem__(self, n):
#         if isinstance(n, int): # n是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice): # n是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
# print(Fib()[2:5])

#只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')


# import logging 
# logging.basicConfig(level=logging.INFO)
# def foo(s):
# 	assert int(s) != 0,'n is zero'
# 	logging.info('hahahaha')
# 	return 10/int(s)
# def bat(s):
# 	return foo(s)*2
# def main():
# 	try:
# 		bat('0')
# 	except Exception as e:
# 		logging.exception(e)
# 	else:
# 		pass
# 	finally:
# 		pass
# main()
# print('END')

# from collections import namedtuple
# Point = namedtuple('Point',['x','y'])
# p = Point(1,2)
# print(p.x,isinstance(p,tuple))

# from collections import deque
# q = deque(['1','2'])

#md5验证
import hashlib

def calc_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user,password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	print(md5.hexdigest())
	if db[user] == md5.hexdigest():
		return True
	return False
def get_md5(token):
	md5 = hashlib.md5()
	md5.update(token.encode('utf-8'))
	return md5.hexdigest()

dbs = {}
def register(user,password):
	db[user] = get_md5(password + user + 'the-Salt')

def log_in(user,password):
	md5 = hashlib.md5()
	token = password + user + 'the-Salt'
	md5.update(token.encode('utf-8'))
	if db[user] == md5.hexdigest():
		return True
	return False
register('michael','123456')
print(log_in('michael','123456'))

