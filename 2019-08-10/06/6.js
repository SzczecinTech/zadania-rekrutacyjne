const numOfChar = (char, string) => string.split(char).length - 1;
const numOfCharWithArray = (char, string) => [...string].filter(c => c === char).length;

console.log(numOfChar('h', 'hello house'));
console.log(numOfCharWithArray('e', 'hello house'));