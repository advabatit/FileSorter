import os
import shutil

def create_folder(path: str, extention: str)->str:
    ''' Function that creats new folder that named after the extenstion variable '''
    folder_name: str = extention[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path

def sort_files(source_path: str)-> None:
    ''' Function that sorts all files to new folders by their extenstion '''
    for (source_dir, sub_dir_list, files) in os.walk(source_path):
        for file in files:
            file_path: str = os.path.join(source_dir, file)
            extention: str = os.path.splitext(file)[1]

            if extention:
                new_folder: str = create_folder(source_path, extention)
                new_path: str = os.path.join(new_folder, file)

                shutil.move(file_path, new_path)

def remove_old_folders(source_path: str) -> bool:
    ''' Function that deletes all old folders from the directory'''

    for (source_dir, sub_dir_list, files) in os.walk(source_path, topdown=False):
        for curr_dir in sub_dir_list:
            folder_path: str = os.path.join(source_dir, curr_dir)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)

def main():
    path = input("Please enter the path: ")
    
    if os.path.exists(path=path):
        sort_files(path)
        remove_old_folders(path)
        print("Files sorted successfully")
    else:
        print("Invalid path")    

main()