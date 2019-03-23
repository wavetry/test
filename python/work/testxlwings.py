#!/usr/python
# coding=utf-8

import csv
datas = [['name', 'age'],
['Bob', 14],
['Tom', 23],
['Jerry', '18']]
# with open('example.csv','w',newline='') as f:
# 	writer = csv.writer(f)
# 	for row in datas:
# 		writer.writerow(row)
# 	
# with open('example.csv') as f:
# 	reader = csv.DictReader(f)
# 	for row in reader:
# 		max_temp = row['name']
# 		print(max_temp)

headers = ['name','age']
datas = [
{'name':'Bob','age':23},
{'name':'H','age':23},
{'name':'E','age':23}
]
with open('example.csv','w',newline='') as f:
	writer = csv.DictWriter(f,headers)
	writer.writeheader()
	for row in datas:
		writer.writerow(row)

	writer.writerows(datas)