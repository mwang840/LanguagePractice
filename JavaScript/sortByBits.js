const sortByBits = function (arr) {
  //First look at the input array
  //Loop over the array and turn them into binary numbers
  //Then count the occurance of ones and then sort the input array from the number of ones in a binary number
  const count = (x) => {
    const str = x.toString(2);
    let num = 0;
    for (const c of str) {
      if (c === "1") {
        num += 1;
      }
    }
    return num;
  };
  return arr.sort((a, b) => {
    const countA = count(a);
    const countB = count(b);
    return countA === countB ? a - b : countA - countB;
  });
};

const main = function () {
  const arr = [0, 1, 2, 3, 4, 5, 6, 7, 8];
  console.log(sortByBits(arr));
};

main();
