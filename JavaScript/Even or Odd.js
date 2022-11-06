// https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

// w ternary
function evenOrOdd(number) {
  return number % 2 == 0 ? 'Even' : 'Odd';
}

// without ternary
function evenOrOdd(number) {
  if (number % 2 == 0) {
    return 'Even'
  }
  return 'Odd'
}
