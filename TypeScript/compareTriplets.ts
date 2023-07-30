

/*
 * Complete the 'compareTriplets' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

function compareTriplets(a: number[], b: number[]): number[] {
    //have a loop for both a and b maybe nested, compare the values of indices and add the scores up in the end
    let aScore = 0;
    let bScore = 0;
    let twos: number[] = [];
    for(let i = 0 ; i < a.length; i++){
        if(a[i] > b[i]){
            aScore += 1;
        }
        else if(a[i] < b[i]){
            bScore += 1;
        }
        
    }
    twos.push(aScore);
    twos.push(bScore);
    return twos;
}


