import re

def get_count(sentence):
    return len(re.findall(r"[aAeEiIoOuU]", sentence))
