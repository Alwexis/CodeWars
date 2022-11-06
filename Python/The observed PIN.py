# https://www.codewars.com/kata/5263c6999e0f40dee200059d

# This one made me cry lol
import itertools

def get_pins(observed):
    tabForEach = {
        '0': ['8', '0'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }
    adjacents = []
    result = []
    for digit in observed:
        adjacents.append(tabForEach[digit])
    possibilities = itertools.product(*adjacents)
    for possibility in possibilities:
        result.append(''.join(possibility))
    return result
