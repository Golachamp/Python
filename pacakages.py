import os
import shutil
print(os.getcwd())
# To check the Disk Space

print(shutil.disk_usage("/"))
#total, used, free = shutil.disk_usage("/")
#print("Total disk space is",total // (2**30))
#print("Total used space is",used // (2**30)) 
#print("Total free space is",free // (2**30))

# F string
total, used, free = shutil.disk_usage("/")
print(f"Total disk space is {total // (2**30)} GB")
print(f"Total used space is {used // (2**30)} GB") 
print(f"Total free space is {free // (2**30)} GB")
