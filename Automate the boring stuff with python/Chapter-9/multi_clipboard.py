import sys ,shelve ,pyperclip

#print(pyperclip.paste())

myshelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        myshelf[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1].lower() == 'delete':   # checks cli [1] have delete
        del myshelf[sys.argv[2]]    # if then taking cli [2] as key delete teh element

if len(sys.argv) == 2:
    if sys.argv[1].lower() == 'delete':     # checks cli [1] have delete if the cli is only 2 index long
        myshelf.clear()           # if then it formats the opened mcb file

    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(myshelf.keys())))

    elif sys.argv[1] in myshelf:
        pyperclip.copy(myshelf[sys.argv[1]])


myshelf.close()
