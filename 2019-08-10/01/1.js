const summer = (...numbers) => numbers.reduce((prev, curr) => prev + curr, 0);

const re = summer(1,2,3);
console.log(re);