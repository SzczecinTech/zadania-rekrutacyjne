const slicesEnough = (slices, recipients, slicesEach) => slices >= recipients * slicesEach;

console.log(slicesEnough(11, 5, 2));