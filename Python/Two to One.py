import re

def longest(a1, a2):
    list = re.findall(r"[a-zA-Z]", a1) + re.findall(r"[a-zA-Z]", a2)
    newList = []
    for char in list:
        if char not in newList:
            newList.append(char)
    newList.sort()
    return ''.join(newList)
