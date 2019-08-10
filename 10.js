const anagram = (a, b) => {
  const arrayA = a.toLowerCase().split('').sort().join('');
  const arrayB = b.toLowerCase().split('').sort().join('');
  return arrayA === arrayB;
}
console.log(anagram('finder', 'Friend'));