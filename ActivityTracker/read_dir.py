import time
# Get the file name from the user provided Path
# function return the file name from the path and also return the count of the file
# the return data type is tuple
# the file name is stored in list and count data type is integer
def get_file_name(dir_path):
    count_file = 0
    file_name = []
    try:
        if dir_path.exists():
            file_list = dir_path.iterdir()

            for item in file_list:
                count_file += 1
                file_name.append(item.name)
        else:
            print('Path does not exist')
    except PermissionError:
        print(f'Permission denied to access {dir_path}')
    return file_name, count_file


# get the detials of file
# file_name, author,last_modified_by, file_size, modified_time, file_created_time 
def get_metadadta(file_path):

    #Get file metadata
    file_size = file_path.stat().st_size
    last_modified = file_path.stat().st_mtime
    last_accessed = file_path.stat().st_atime
    creation_time = file_path.stat().st_ctime
    
    print(file_size, time.ctime(last_modified), time.ctime(last_accessed), time.ctime(creation_time))

    return 0