# One line
def is_valid_walk(walk):
    return (walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')) and len(walk) == 10
  
# More than one
def is_valid_walk(walk):
    if (walk.count('n') == walk.count('s') and 
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True
    return False
