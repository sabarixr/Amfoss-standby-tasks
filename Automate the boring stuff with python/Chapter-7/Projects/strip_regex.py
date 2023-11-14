import re

def strippp(txt, argumet=''):
    if argumet == '':
        strx = re.compile(r'^\s+|\s+$')
        mo = strx.sub('', txt)
        print(mo)
    else:
        strx = re.compile(argumet)
        mo = strx.sub('', txt)
        print(mo)


text = '        TEsting text 23  '
strippp(text, 'e')
strippp(text)
