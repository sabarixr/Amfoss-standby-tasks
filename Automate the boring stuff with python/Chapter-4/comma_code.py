def commacode(list1):
    if len(list1) == 1:
        return list1[0]
    elif len(list1) == 0:
        return "provide a list to execute the function"
    else:
        sentence = ', '.join(list1[:-1]) + ' and ' + list1[-1]
        return sentence


spam = ['apples', 'bananas', 'tofu', 'cats']


answer = commacode(spam)
print(answer)
