var climbStairs = function (n) {
  if (n <= 1) {
    return n;
  }
  const stairs = new Array(n + 1);
  stairs[1] = 1;
  stairs[2] = 2;
  for (let i = 3; i <= n; i++) {
    stairs[i] = stairs[i - 1] + stair[i - 2];
  }
  return stairs[n];
};
