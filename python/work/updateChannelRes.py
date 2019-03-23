#!/usr/python
# coding=utf-8

import os,sys,getopt,shutil

SRC = "juhao"

# SRC_CCS_SUBGAME = SRC + "\\cocosstudio\\subgame"
SRC_RES_SUBGAME = SRC + "\\res\\subgame"

SRC_RUNTIME = SRC + "\\runtime"
def search(path):
	dirs_files = os.listdir(path)
	for file_name in dirs_files:
		full_path = os.path.join(path,file_name)

		if os.path.isdir(full_path):
			if file_name != SRC:
				# del_ccs_path = os.path.join(path,file_name + "\\cocosstudio\\subgame")
				del_res_path = os.path.join(path,file_name + "\\res\\subgame")
				del_run_path = os.path.join(path,file_name + "\\runtime")

				if os.path.exists(del_res_path):
					shutil.rmtree(del_res_path)
				if os.path.exists(del_run_path):
					shutil.rmtree(del_run_path)
				# os.mkdir(del_ccs_path)
				# os.mkdir(del_res_path)
				# shutil.copytree(SRC_CCS_SUBGAME, del_ccs_path)
				print("copy files from "+SRC_RES_SUBGAME+" to "+del_res_path)
				shutil.copytree(SRC_RES_SUBGAME, del_res_path)
				print("copy files from "+SRC_RUNTIME+" to "+del_run_path)
				shutil.copytree(SRC_RUNTIME, del_run_path)
				
			
if __name__ == '__main__':
	print("copy files start",os.path.split(os.path.realpath(__file__))[0])
	try:
		search(os.path.split(os.path.realpath(__file__))[0])
	except:
		with open("xx.log", "w+") as f:
			f.write(str(sys.exc_info()))		
	os.system("pause")
