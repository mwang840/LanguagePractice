function largestSumOfAverages(nums: number[], k: number): number {
    //For an given array of length n, we split that array into k subsets
    //Given those k subsets we add the sum of each subset
    //divide and add if needed
    
    const MAXSIZE = 100000000000000000;
    let averageTable: number[][] = new Array(MAXSIZE).fill(0).map(() => new Array(MAXSIZE).fill(0));
    for(let i = 1; i < nums.length; i++){
        for(let j = 1; j <=k; j++){
            for(let l = 0; l < i; l++){
                averageTable[i][j] = Math.max()
            }
        }
    }
    return -1;
};