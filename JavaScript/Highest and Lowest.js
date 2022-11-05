// https://www.codewars.com/kata/554b4ac871d6813a03000035
function highAndLow(numbers){
  const newNumbers = numbers.split(' ').sort((a, b) => { return a - b });
  return `${newNumbers[newNumbers.length - 1]} ${newNumbers[0]}`
}
