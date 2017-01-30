import os

def rename_files():
	file_list = os.listdir(r"1")
	saved_path = os.getcwd()
	print('Saved path is ' +saved_path)
	os.chdir(r"1")
	for file_name in file_list:
		os.rename(file_name,file_name.translate(str.maketrans('','','1234567890')))


rename_files()