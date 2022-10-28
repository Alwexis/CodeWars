import re
# Whoever reading this. Learn RegEx. Its useful af
def to_camel_case(text):
    words = re.findall(r"[a-zA-Z]+", text)
    str = ''
    for x in words:
        str += x.capitalize() if words.index(x) > 0 else x
    return str
