# https://www.codewars.com/kata/55b42574ff091733d900002f

# The simple one
def friend(x):
    return [person for person in x if len(person) is 4]
    
# Another way to do the same as above, but more readable
def friend(x):
    friends = []
    for person in x:
        if len(person) is 4:
            friends.append(person)
    return friends
