// https://www.codewars.com/kata/55d24f55d7dd296eb9000030
var summation = function (num) {
  let summation = 0;
  for (let x = 0; x < num + 1; x++) {
    summation += x;
  }
  return summation;
}
