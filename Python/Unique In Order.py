def unique_in_order(iterable):
    newList = []
    for x in iterable:
        if len(newList) == 0:
            newList.append(x)
        if newList[-1] != x:
            newList.append(x)
    return newList
