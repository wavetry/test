#!/usr/python
# coding=utf-8
import os

log_fd = open('work.log','w+')

def write_log(log_str):
	print(log_str)
	log_fd.write(log_str )
	log_fd.write('\n')
	log_fd.flush()

def exec_cmd(cmd_str):
	ret = os.popen(cmd_str).read()
	write_log(ret)

