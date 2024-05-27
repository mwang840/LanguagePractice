function sumPairs(ints: number[], s: number): [number, number] | void {  
    let leftPair = 0;
    let rightPair = ints.length - 1;
    let pairStack: number[] = [];
    let currentIndexPair: number[] = []
    while(leftPair < rightPair){
        const currentSum = ints[leftPair] + ints[rightPair];
        if(currentSum < s){
            leftPair +=1;
        }
        else if(currentSum > s){
            rightPair -=1;
        }
        else{
            pairStack.push(ints[leftPair], ints[rightPair]);
            currentIndexPair.push(leftPair, rightPair);
            return [ints[leftPair], ints[rightPair]];
        }
    }

    return undefined; // your code here
}

function main(){
    console.log(sumPairs([11, 3, 7, 5],         10));
}

main()