from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print('Current data and time: ', current_time)

str_current_datetime = str(current_time)

file_name = str_current_datetime + ".txt"
# file_name = str_current_datetime+".csv"
file = open('./TestFiles/'+file_name,'w')

print('File created: ', file.name)
file.close()