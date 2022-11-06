# https://www.codewars.com/kata/56269eb78ad2e4ced1000013

import math

def find_next_square(sq):
    nextSquare = (math.sqrt(sq) + 1) ** 2
    if nextSquare % 1 == 0.0:
        return nextSquare
    return -1
