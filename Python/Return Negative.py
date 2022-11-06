# https://www.codewars.com/kata/55685cd7ad70877c23000102

# Con Ternary
def make_negative( number ):
  return number * -1 if number > 0 else number

# Sin Ternary
def make_negative( number ):
  if number > 0:
    return number * -1
  return number
