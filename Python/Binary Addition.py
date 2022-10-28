def add_binary(a,b):
    sum = a + b
    binary = ''
    while sum > 0:
        mod = sum % 2
        binary += str(mod)
        sum = sum // 2
    return binary[::-1]
