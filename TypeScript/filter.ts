export const getEvenNumbers = (numbersArray: number[]) : number[]=>{
    return numbersArray.filter(element => element % 2 == 0);
}