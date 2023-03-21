import os
import shutil

oridatadir = '/workspace/share/kitreg/data/scene_classify/kitchen'
targetdatadir = '/workspace/share/beit3/data/kitchen'

# 创建目标文件夹
os.makedirs(targetdatadir, exist_ok=True)

# 循环遍历oridatadir下的所有文件夹
for foldername in os.listdir(oridatadir):
    folderpath = os.path.join(oridatadir, foldername)
    if os.path.isdir(folderpath):
        print(f'Processing folder: {folderpath}')
        # 遍历train、val、test三个文件夹
        for subfoldername in os.listdir(folderpath):
            subfolderpath = os.path.join(folderpath, subfoldername)
            if os.path.isdir(subfolderpath):
                # 将subfolderpath下的所有文件和子文件夹复制到targetdatadir下
                targetsubfolderpath = os.path.join(targetdatadir, subfoldername)
                shutil.copytree(subfolderpath, targetsubfolderpath, dirs_exist_ok=True)
                print(f'Copied {subfolderpath} to {targetsubfolderpath}')
