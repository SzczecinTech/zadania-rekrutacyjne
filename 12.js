const fetch = require('isomorphic-fetch');
const fetchPos = () => fetch('http://api.open-notify.org/iss-now.json')
  .then(response => response.json());

const getDeltaAngle = (posA, posB) => {
  const deltaLatitude = posB.iss_position.latitude - posA.iss_position.latitude;
  const deltaLongitude = posB.iss_position.longitude - posA.iss_position.longitude;
  return Math.sqrt(Math.pow(deltaLatitude, 2) + Math.pow(deltaLongitude, 2));
}
const app = async () => {
  const firstPos = await fetchPos();
  const positions = [firstPos];
  setInterval(async () => {
    const newPos = await fetchPos();
    positions.push(newPos);
    if (positions.length > 1) {
      const a = positions[positions.length - 2];
      const b = positions[positions.length - 1];
      const deltaTime = b.timestamp - a.timestamp;
      const deltaAngle = getDeltaAngle(a, b);
      console.log('delta time', deltaTime);
      console.log('delta angle', deltaAngle);
      console.log('speed rad/s', deltaAngle / deltaTime);
      
      console.log('speed km/s', deltaAngle * 110 / deltaTime);
      console.log('speed km/h', deltaAngle * 110 / (deltaTime / 60 / 60));
      
      console.log('distance', getDeltaAngle(firstPos, b) * 110);
    }
  }, 1000);
}
app();