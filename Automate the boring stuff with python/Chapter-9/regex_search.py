import re
import pyinputplus as pyi
from pathlib import Path
from os import listdir
total_lines = 0

find_case = pyi.inputStr(prompt='Enter the expression you8 want to check : ')
find_asergx = re.compile(find_case)

pat = str( str(pyi.inputFilepath(prompt='Enter the path to the dictionary: ')))
grp_files = listdir(pat)
for file in grp_files:
    if file.endswith('.txt'):
        file_op = open(Path(pat)/file)
        for line in file_op:

            match_case = find_asergx.findall(line)
            for matches in match_case:
                print(f'\n{matches} was found in {line} of  file - {file}')

print('\ncompleted execution')



