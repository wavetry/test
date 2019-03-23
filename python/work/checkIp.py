#!/usr/python
# coding=utf-8
 
import socket,sys,os


def checkIp(sk,host,port):
	port = int(port)
	return sk.connect_ex((host,port))

if __name__ == '__main__':
	argv = sys.argv
	if not os.path.exists('ip_port.txt'):
		print "ip_port.txt file not exists"
		os.system("pause")
	if os.path.exists('failedIP.txt'):
		os.popen('rm failedIP.txt')
	fd = open("failedIP.txt",'w+')

	with open('ip_port.txt') as f:
		for line in f:
			address = line.strip().split('_')
			sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			result = checkIp(sk,address[0],address[1])
			if result != 0:
				fd.write(line)
				fd.flush()
				print("%s connect failed" % line.strip())
			else:
				print("%s connect succ" % line.strip())
				sk.close()
	fd.close()
	os.system("pause")