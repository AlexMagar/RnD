from read_dir import *
from pathlib import Path

def get_folder_path():
    path_name = input('Please enter the path name: ')
    return path_name

# get file name to get the details
def get_file_path():
    file_path = input('Please enter name of file for metadata: ')
    return file_path

def main():
    file_path = Path(get_folder_path())
    file_name = Path(get_file_path())
    abc = get_file_name(file_path)
    ghi = get_metadadta(file_name)
    print('Activities Tracker: ', abc[1])

if __name__ == '__main__':
    main()

# nth to print here