const zeroFuel = (distanceToPump, mpg, fuelLeft) => {
  const makeIt = mpg * fuelLeft - distanceToPump;
  return makeIt >= 0 ? true : false;
};
