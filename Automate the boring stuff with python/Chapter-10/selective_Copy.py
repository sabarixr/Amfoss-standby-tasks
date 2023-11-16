import shutil
import os
from pathlib import Path
import pyinputplus as pyin

fold_t = pyin.inputFilepath(prompt='Input file path to the folder you want to walk: ')
exte_n = pyin.inputStr(prompt='Enter the extension you want to search: ')
fold_new = pyin.inputFilepath(prompt='Input file path to the folder you want to copy the files to: ')

if not os.path.exists(fold_new):
    os.makedirs(fold_new)

for folder_name, sub_folders, filenames in os.walk(fold_t):
    for file in filenames:
        if file.endswith(exte_n):
            file_Path = Path(folder_name) / file
            new_fold = Path(fold_new) / file

            shutil.copy(file_Path, new_fold)
            print(f'Copied {file} to the specified folder')
