// https://www.codewars.com/kata/53dc54212259ed3d4f00071c

// forEach and readable one
function sum (numbers) {
  let sum = 0;
  numbers.forEach(number => sum += number);
  return sum;
};

// Reduce one
function sum(numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
