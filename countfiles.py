import os

def count_files_in_folder(folder_path):
    count = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        count += len(filenames)
    return count

folder_path = "/workspace/share/kitreg/data/scene_classify/kitchen"
file_count = count_files_in_folder(folder_path)
print(f"There are {file_count} files in {folder_path} and its subfolders.")