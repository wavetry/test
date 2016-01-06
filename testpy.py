# -*- coding: utf-8 -*-
def fa(x):
	if not isinstance(x,(int ,float)):
		raise TypeError('error')
	if x <=1:
		return 1	
	else:
		return x


def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

##**kw means dictionary 
def person(name,age,**kw):
	print('name:', name, 'age:', age, 'other:', kw)

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def man(name, *,age):
	print(name,age)

#递归
def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n - 1)
#递归会溢出,可以用尾递归优化
def factx(n):
	return fact_iter(n,1)
def fact_iter(num,pro):
	if num == 1:
		return pro
	return fact_iter(num - 1,num * pro)
#汉诺塔问题

def move(n,a,b,c):
	if n==1:
		print('move',a,'-->',c)
		return
	move(n-1,a,c,b)
	print('move',a,'-->',c)
	move(n-1,b,a,c)

#斐波那契数列
def fbnc(n):
	if n==1 or n==0:
		return n
	return fbnc(n-1)+fbnc(n-2)

#杨辉三角
def triangles1():
	b = [1]
	i=0
	while True:
		yield b
		b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
		print(b)

def triangles2():
    L=[1,]
    while(True):
        yield L 
        i=len(L)-1
        while(i):
            L[i]=L[i]+L[i-1]
            i-=1
        L.append(1)

# n=0
# for t in triangles():
#     print (t)
#     n=n+1
#     if n==10:
#         break
from functools import reduce
def str2float(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(lambda x,y:x*10+y,map(char2num,s.replace('.','')))/(10**s[::-1].find('.') if s.find('.')!=-1 else 1)

def _odd_iter():
	n=1
	while True:
		n+=2
		yield n

def _not_divisible(n):
	return lambda x:x%n>0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n=next(it)
		yield n
		it = filter(_not_divisible,it)
#文件读写 'r'read 'rb'read in binary 'w'write 'wb'write in binary
# with open('test.lua','r',encoding = 'gbk',errors = 'ignore') as f:
# 	print(f.read(100))
# 	# for lines in f.readlines():
# 	# 	print(lines.strip())

# with open('test.txt','w',encoding = 'utf-8')as f:
# 	f.write('Hello Woarld')


# def by_name(t):
# 	return t[0].lower()
# def by_score(t):
# 	return t[1]
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=by_name)
# print(L2)
# L2 = sorted(L, key=by_score,reverse=True)
# print(L2)

# [x for x in os.listdir('.') if os.path.isdir(x)]
# [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#json
import json

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
	
def student2dict(std):
		return {
	    	'name': std.name,
	    	'age': std.age,
	    	'score': std.score
	    	}
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))

print(json.dumps(s, default=lambda s: s.__dict__))

