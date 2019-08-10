const fizzBuzz = n => {
  new Array(n)
    .fill()
    .forEach((v, i) => {
      const number = i + 1;
      const per3 = number % 3 === 0;
      const per5 = number % 5 === 0;
      if (per3 && per5) {
        console.log('FizBuzz');
      } else if (per3) {
        console.log('Fizz');
      } else if (per5) {
        console.log('Buzz');
      } else {
        console.log(number);
      }
    })
}
fizzBuzz(25);