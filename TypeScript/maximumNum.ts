function rowAndMaximumOnes(mat: number[][]): number[] {
  let index = 0;
  let count = 0;
  for (let i = 0; i < mat.length; i++) {
    let countOnes = 0;
    for (let j = 0; j < mat[i].length; j++) {
      countOnes += mat[i][j];
      if (countOnes > count) {
        count = countOnes;
        index = i;
      }
      if (countOnes === mat[i].length + 1) {
        break;
      }
    }
  }
  return [index, count];
}
