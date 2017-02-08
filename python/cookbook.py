# * use
*a,b = [1,2,3,4,5]
print (a)

#deque 
from collections import deque

def search(lines ,pattern,history=5):
	pre_line = deque(maxlen=history)
	for li in lines:
		if pattern in li:
			yield li,pre_line
		pre_line.append(li)

import heapq

#nlargest nsmallest
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap,expensive)