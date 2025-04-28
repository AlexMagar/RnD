import os
from path import Path
import datetime
import time

# get the current working directory
cwd = os.getcwd()

cwd = Path('/Users/StuffMy/prog/XDataMining')

for file in cwd.files():
    file_name = file
    last_Mod = os.stat(file).st_ctime
    into_str = str(datetime.datetime.strptime(time.ctime(last_Mod),"%a %b %d %H:%M:%S %Y"))
    size = str(os.stat(file).st_size)

    # write in 
    file = open('./TestFiles/RecordActivities.txt','a')

    file.write(file_name)
    file.write(size)
    file.write(into_str + '\n')
    
    print("File name: ",file_name)
    print("File Size inbytes: ",size)
    print("Date time: ",datetime.datetime.strptime(time.ctime(last_Mod),"%a %b %d %H:%M:%S %Y"))


file.close()

