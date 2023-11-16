import re
import pyinputplus as pyi
from pathlib import Path

pt = str(pyi.inputFilepath(prompt='Enter the path to the file(./file - if its in the current dictionary): '))
file_op = open(pt, 'r')
file_r = file_op.read()
file_op.close()

filergx = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
finds = filergx.findall(file_r)
print(file_r)

for i in finds:
    inp = pyi.inputStr(prompt=f'enter {i}: ')
    file_r = re.sub(i, inp, file_r)

print(file_r)
st_gplace = Path(pt)
newfile = Path(st_gplace.parent/'updated_newfile.txt') # .parent gives the parent file ofg the file we opened earlier so i am adding the newly opened file to teh same dictionary

update_new = open(newfile,'w')
newfile.write_text(file_r)
print('done')