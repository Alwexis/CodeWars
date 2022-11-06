// https://www.codewars.com/kata/56676e8fabd2d1ff3000000c

// Simplest way
function findNeedle(haystack) {
  return 'found the needle at position ' + haystack.indexOf('needle')
}

// For loop way
function findNeedle(haystack) {
  let index = -1;
  for (let thing of haystack) {
    index++;
    if (thing === 'needle') {
      return index;
    }
  }
}
