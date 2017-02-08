# # _*_ coding:utf-8 _*_
# #第一题
# import urllib
# import re

# tmp_re=urllib.urlopen('http://www.heibanke.com/lesson/crawler_ex00/')
# html=tmp_re.read()
# index=re.findall(r'输入数字([0-9]{5})',html)

# while index:
# 	url='http://www.heibanke.com/lesson/crawler_ex00/%s/' % index[0]
# 	print url
# 	tmp_re=urllib.urlopen(url) 
# 	html=tmp_re.read()
# 	index=re.findall(r'数字是([0-9]{5})',html)
# print html


# # _*_ coding:utf-8 _*_
# #第二题
# import urllib
# import re

# data={'username':'Tom'}
# url='http://www.heibanke.com/lesson/crawler_ex01/'

# for num in range(1,31):
# 	data['password']=num
# 	post_data=urllib.urlencode(data)
# 	print post_data
# 	response=urllib.urlopen(url,post_data)
# 	html=response.read()
# 	result=re.findall('密码错误',html)
# 	if not result:
# 	        print html
# 	        break



# _*_ coding:utf-8 _*_
#第三题
import requests
import re

login_data={'username':'昵称','password':'密码'}
url='http://www.heibanke.com/lesson/crawler_ex02/'
login_url='http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'

r2=requests.get(login_url)
c2=r2.cookies

login_data['csrfmiddlewaretoken']=c2['csrftoken']
r3=requests.post(login_url,data=login_data,allow_redirects=False,cookies=c2)
c3=r3.cookies

pass_data={'username':'tom','csrfmiddlewaretoken':c3['csrftoken']}
for passwd in range(31):
	print passwd
	pass_data['password']=passwd
	r5=requests.post(url,pass_data,cookies=c3)
	result=re.findall(r'密码错误',r5.text.encode('utf-8'))
	if not result:
	        print r5.text
	        break

# # _*_ coding:utf-8 _*_
# import requests
# import re
# import threading
# import Queue


# data={'username':'账户','password':'密码'}
# url='http://www.heibanke.com/lesson/crawler_ex03/'
# login_url='http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'
# passwd_url='http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page=%s'

# r1=requests.get(login_url)
# c1=r1.cookies

# data['csrfmiddlewaretoken']=c1['csrftoken']
# r2=requests.post(login_url,data=data,allow_redirects=False,cookies=c1)
# c2=r2.cookies

# data2={'username':'tom','csrfmiddlewaretoken':c2['csrftoken']}

# def getpasswd(page):
#     print passwd_url % page
#     r4=requests.get(passwd_url % page,cookies=c2)
#     pos=re.findall('password_pos">([0-9]*)</td>',r4.text)
#     val=re.findall('password_val">([0-9]*)</td>',r4.text)
#     for i in range(len(pos)):
#             dict[int(pos[i])]=val[i]
#     q.put('ok')
#     print len(dict)

# dict={}
# q=Queue.Queue()

# for i in range(1,3):
#     q.put('ok')

# while len(dict)!=100:
#     for page in range(1,14):
#         if q.get():
#             t=threading.Thread(target=getpasswd,args=(page,))
#             t.start()
#         if len(dict)==100:
#             break	

# passwd=''
# ks=dict.keys()
# ks.sort()

# for k in ks:
#     print k,dict[k]
#     passwd=passwd + dict[k]

# data3={'username':'tom','password':passwd,'csrfmiddlewaretoken':c2['csrftoken']}
# r5=requests.post(url,data=data3,cookies=c2)
# print r5.text
