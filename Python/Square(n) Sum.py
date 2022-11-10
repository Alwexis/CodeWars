# https://www.codewars.com/kata/515e271a311df0350d00000f

# one line (but not readable at all) method
def square_sum(numbers):
  return sum(x ** 2 for num in numbers)

# for loop method
def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
