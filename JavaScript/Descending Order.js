// https://www.codewars.com/kata/5467e4d82edf8bbf40000155
function descendingOrder(n) {
  let number = String(n).split('').sort((a, b) => { return b - a }).join('');
  return parseInt(number)
}
