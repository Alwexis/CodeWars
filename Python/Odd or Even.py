# https://www.codewars.com/kata/5949481f86420f59480000e7

# Ternary & Math module way
import math

def odd_or_even(arr):
    return 'even' if math.fsum(arr) % 2 == 0 else 'odd'
    
# without math module and ternary at all
def odd_or_even(arr):
  totalSum = 0
  for x in arr:
    totalSum += x
  if totalSum % 2 == 0:
    return 'even'
  else:
    return 'odd'
