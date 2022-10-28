def square_digits(num):
    newStr = ''
    numStr = str(num)
    for x in numStr:
        newStr += str(int(x) * int(x))
    return int(newStr)
