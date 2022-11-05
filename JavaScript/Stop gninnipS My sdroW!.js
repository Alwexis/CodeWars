// https://www.codewars.com/kata/5264d2b162488dc400000001
function spinWords(string){
  let words = string.split(" ");
  words.forEach((word, index) => {
    if (word.length >= 5) {
      words[index] = word.split("").reverse().join("");
    }
  })
  return words.join(" ");
}
