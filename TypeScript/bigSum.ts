function aVeryBigSum(ar: number[]): number {
    // Write your code here
    return ar.reduce((long:number, num: number)=>long + num, 0);
}