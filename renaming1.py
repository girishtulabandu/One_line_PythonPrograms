import os
os.chdir('folder_path')    # please add the path to your folder inside quotes
i=['0','1','2','3','4']
k=0
for f in os.listdir():
    name,ext=os.path.splitext(f)
    newname='{}{}'.format(i[k],ext)
    os.rename(f,newname)
    print(f)
    k=k+1
   
for f in os.listdir():   
    print(f)
	
	
	#this program renames all the files in a particular folder in order of created date time