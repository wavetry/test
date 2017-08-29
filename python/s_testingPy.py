#-*- coding: utf-8 -*-
# from PIL import Image,ImageDraw,ImageFont 0000

# originl_avatar = "test.jpg"
# save_avatar = "new_avatar.jpg"
# windows_font = "Arial.ttf"
# color = (255,0,0)

# def draw_text(text,fill_color,windows_font):
# 	print("do some")
# 	try:
# 		im = Image.open(originl_avatar)
# 		x,y = im.size
# 		print(im.size,im.format,im.mode)
# 		im.show()

# 		draw = ImageDraw.Draw(im)
# 		font = ImageFont.truetype(windows_font,35)
# 		draw.text((x - 20,7),text,fill_color,font)
# 		im.save(save_avatar)
# 		im.show()
# 	except :
# 		print("Unable to load Image")


# number = str("4")
# draw_text(number,color,windows_font)

#生成随机密钥
# -*- coding: utf-8 -*- 0001
import random,string
import MySQLdb

db = MySQLdb.connect("localhost","root","964711246lzl","coupon")
cursor = db.cursor()


class LengthError(ValueError):
	"""docstring for LengthError"""
	def __init__(self, arg):
		super(LengthError, self).__init__()
		self.arg = arg
def pad_zero_to_left(inputNumString,totalLength):
	lengthOfInput  = len(inputNumString)
	if lengthOfInput > totalLength:
		raise LengthError("error")
	else:
		return '0' * (totalLength - lengthOfInput) + inputNumString

poolOfChars = string.ascii_letters + string.digits
random_codes = lambda x,y:''.join([random.choice(x) for i in range(y)])

def invitation_code_generator(quantity,lengthOfRandom,LengthOfKey):
	placeHoldChar = "L"
	for index in range(quantity):
		tempString = ""
		try:
			yield random_codes(poolOfChars, lengthOfRandom) + placeHoldChar + pad_zero_to_left(str(index), LengthOfKey)
		except LengthError:
			print "Index exceeds the length of master key."

for invitationCode in invitation_code_generator(200,10,4):
    sql = """INSERT INTO table1(coupon)
            VALUE ('%s')
        """ % invitationCode
    
    try:
        cursor.execute(sql)
        db.commit()
        print( sql)
    except Exception, e:
        print(e)
        db.rollback()
db.close()


	
# from multiprocessing import Pool 
# import os,time,random

# def long_time_task(name):
# 	print("Run task %s (%s) ..." % (name,os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print("Task %s runs %0.2f seconds." % (name , (end - start)))

# if __name__ == '__main__':
# 	print ("Parent process %s." % os.getpid())
# 	p = Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_time_task,args=(i,))
# 	print("Waiting for all subprocessed done...")
# 	p.close()
# 	p.join()
# 	print('All subprocessed done')


# import subprocess

# print('nslookup')
# r = subprocess.call(['nslookup','wavetry.shop'])
# print('Exit code:',r)

# import subprocess

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# from multiprocessing import Process,Queue
# import os,time,random

# def write(q):
# 	print('Process to write :%s' % os.getpid())
# 	for value in ['A','B','C']:
# 		print('Put %s to Queue ...' % value)
# 		q.put(value)
# 		time.sleep(random.random())
# def read(q):
# 	print ('Process to read %s ' % os.getpid())
# 	while True:
# 		value = q.get(True)
# 		print('Get %s from queue' % value)




# if __name__ == '__main__':
# 	q = Queue()
# 	pw = Process(target=write,args = (q,))
# 	pr = Process(target=read,args = (q,))
# 	pw.start()
# 	pr.start()
# 	pw.join()
# 	pr.terminate()


# import time,threading

# def loop():
# 	print('thread %s is running ...' % threading.current_thread().name)
# 	n = 0
# 	while n < 5 :
# 		n = n + 1
# 		print('thread %s >>> %s' % (threading.current_thread().name,n))
# 		time.sleep(1)
# 	print('thread %s ended' % threading.current_thread().name)

# print('thrad %s is running ...' % threading.current_thread().name)
# t = threading.Thread(target=loop)
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


import time, threading

# 假定这是你的银行存款:
balance = 0

lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
    	lock.acquire()
    	try:
    		change_it(n)	
    	finally:
    		lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)