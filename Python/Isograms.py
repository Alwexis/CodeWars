# https://www.codewars.com/kata/54ba84be607a92aa900000f1
def is_isogram(string):
    for char in string.lower():
        if string.lower().count(char) > 1:
            return False
    return True
