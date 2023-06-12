import os
import shutil
print(os.getcwd())
#print(shutil.disk_usage("/"))
total, used, free = shutil.disk_usage("/")
print("Total disk space is",total // (2**30))
print("Total used space is",used // (2**30)) 
print("Total free space is",free // (2**30))
