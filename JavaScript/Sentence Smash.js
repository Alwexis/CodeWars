// https://www.codewars.com/kata/53dc23c68a0c93699800041d

// Join way
function smash (words) {
  return words.join(' ');
};

// Loops Way
function smash(words) {
  newWord = '';
  for (let word of words) {
    newWord += word + ' ';
  }
  return newWord.trim()
}
