const numOfChar = (char, string) => string.split(char).length - 1;

console.log(numOfChar('h', 'hello house'));
console.log(numOfChar('e', 'hello house'));