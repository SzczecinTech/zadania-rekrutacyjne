const isPalindrome = (string) => {
  const lower = string.toLowerCase().replace(/[,.!\s]/g, '');
  return lower === [...lower].reverse().join('');
}
console.log(isPalindrome('fds'));
console.log(isPalindrome('fdsdf'));
console.log(isPalindrome('Wódy żal dla żydów.'));