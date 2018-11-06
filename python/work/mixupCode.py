#
import hashlib,os,shutil
import random
import string

md5=hashlib.md5('app'.encode('utf-8')).hexdigest()

sample_path = "C:\\sample\\"
def search(path):
	dirs_files = os.listdir(path)

	for file_name in dirs_files:
		full_path = os.path.join(path,file_name)
		if os.path.isdir(full_path):
			for index in range(random.randint(1,5)):
				ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
				ran_str = hashlib.md5(ran_str.encode('utf-8')).hexdigest()
				new_dir = os.path.join(path,ran_str)
				os.mkdir(new_dir)

				for i in range(random.randint(1,5)):
					sample_list = os.listdir(sample_path)
					sample_file = sample_list[random.randint(0,len(sample_list) - 1)]
					# print(sample_file)

					src_path = os.path.join(sample_path,sample_file)
					shutil.copy(src_path,new_dir)
					md5=hashlib.md5(sample_file.encode('utf-8')).hexdigest()
					file_ext = sample_file.split(".")[-1]
					md5 = md5 + "." + file_ext
					# print(os.path.join(new_dir,sample_file),os.path.join(new_dir,md5))
					if not os.path.exists(os.path.join(new_dir,md5)):
						os.rename(os.path.join(new_dir,sample_file),os.path.join(new_dir,md5))
					

			search(full_path)

		file_ext = file_name.split(".")[-1]

		md5=hashlib.md5(file_name.encode('utf-8')).hexdigest()
		if not os.path.isdir(full_path):
			md5 = md5 + "." + file_ext
		print (full_path,os.path.join(path,md5))
		if not os.path.exists(os.path.join(path,md5)):
			os.rename(full_path,os.path.join(path,md5))
if __name__ == "__main__":
	root_path = u'E:\\project\\client_dw\\src\\'
	root_path = u'C:\\test\\'
	search(root_path)