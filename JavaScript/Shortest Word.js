// https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

function findShort(s) {
  const wordArray = s.split(' ').map(word => word.length).sort((a, b) => a - b);
  return wordArray[0];
}

// Readable one
function findShort(s) {
  const arrayPalabras = s.split(' ');
  let masCorta;
  for (let palabra of arrayPalabras) {
    if (palabra.length < masCorta) {
      masCorta = palabra.length;
    }
  }
  return masCorta;
}
