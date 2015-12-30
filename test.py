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
# s = set([12,3,45])
# print(s)
# s.remove(12)
# s.add(45)
# d = set([2,4,5])
# print(s|d)

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

def log(func):
	def wrapper(*args,**kw):
		print('call %s:'%func.__name__)
		return func(*args,**kw)
	return wrapper(*args,**kw)
@log
def now():
	print("now")
now()
