import os
import shutil
from pathlib import Path
import re
import pyinputplus as pyin


folder = pyin.inputFilepath(prompt='Input file path to the folder you want to walk: ')

patten = pyin.inputStr(prompt='Enter the extension you want to search: ')

match_file = re.search(r"(\D*)(\d*)", patten)
if match_file is None:
    print("THE input is wrong")
while not os.path.isdir(folder):
    print('provided folder is wrong')

letters = match_file.group(1)
number_prefix_length = len(match_file.group(2))

os.chdir(folder)


file_list = []
for file_name in os.listdir("."):
    if patten in file_name:
        file_list.append(file_name)

number_list = []
for file_name in file_list:
    match = re.search(r"\d+", file_name)
    if match:
        number_list.append(int(match.group()))

for order_no, number in enumerate(range(1, max(number_list) + 1), 1):
    if order_no not in number_list:
        zeroes_to_add = "0" * (number_prefix_length - len(str(order_no)))
        suffix = Path(file_list[0]).suffix
        n_name = f'{letters}{zeroes_to_add}{order_no}{suffix}'
        shutil.move(file_list[-1], n_name)
        #print(file_list[-1] , n_name)
        print('Renamed')



