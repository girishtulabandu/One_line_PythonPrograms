import glob
import os

directory=os.getcwd()  # 'C:\Users\mahabarat'
os.chdir(directory)
files=glob.glob('*')
for filename  in files:
    if os.stat(filename).st_size<100:
	   os.unlink(filename)

#deletes the files which are having lesser than 100KB size in current folder