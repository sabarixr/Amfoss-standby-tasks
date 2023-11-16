import shutil
import os
from pathlib import Path
import pyinputplus as pyin

folder = pyin.inputFilepath(prompt='Input file path to the folder you want to walk: ')
folder_path = Path(folder).absolute()
for folder_name, sub_folders, filenames in os.walk(folder_path):
    for file in filenames:
        ab_file = Path(folder_name) / file
        size = int(os.path.getsize(ab_file))
        if size > 100000:
            os.unlink(ab_file)
            print(f'deleting {file} from {folder_name}')

print('done deleting')