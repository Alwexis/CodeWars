# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

def reverse_words(text):
    txtArray = []
    for x in text.split(' '):
        txtArray.append(x[::-1])
    return ' '.join(txtArray)
