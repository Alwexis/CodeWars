import math
# Math module is funny
def get_middle(s):
    if len(s) / 2 % 1 == 0:
        ceiledLength = math.ceil(len(s) /2 )
        return s[ceiledLength-1:ceiledLength+1]
    else:
        return s[math.floor(len(s)/2)]
