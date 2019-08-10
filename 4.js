const factorial = n => {
  if (n === 1 || n === 0) {
    return 1;
  }
  return factorial(n - 1) * n;
}
console.log(factorial(0));
console.log(factorial(3));
console.log(factorial(4));