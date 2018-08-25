/**
 * Shuffles array in place. ES6 version
 * @param {Array} a items An array containing the items.
 */
export const shuffle = (a) => {
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
};

export const randomIntFromInterval = (min, max, notIn = null) => {
  let rnd = Math.floor(Math.random() * (max - min + 1) + min);
  if (notIn === null) {
    return rnd;
  }
  while (notIn.includes(rnd)) {
    rnd = Math.floor(Math.random() * (max - min + 1) + min);
  }
  notIn.push(rnd);
  return rnd;
};
