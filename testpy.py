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