# https://www.codewars.com/kata/56541980fa08ab47a0000040

import re

def printer_error(s):
    errors = 0
    for char in s:
        if len(re.findall(r"[a-m]", char)) == 0:
            errors += 1
    return f'{errors}/{len(s)}'
