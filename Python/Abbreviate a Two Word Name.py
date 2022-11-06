# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3

def abbrev_name(name):
    firstName, lastName = name.split(' ')
    return f'{firstName[0].upper()}.{lastName[0].upper()}'
