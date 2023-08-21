function plusMinus(arr: number[]): void {
    // Write your code here
    let positiveNums = 0; 
    let negativeNums = 0; 
    let zeros: number = 0;
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            positiveNums = positiveNums + 1;
        }
        else if(arr[i]  < 0){
            negativeNums = negativeNums + 1;
        }
        else if(arr[i] === 0){
            zeros = zeros + 1;
        }
    }

    console.log(positiveNums / arr.length);
    console.log(negativeNums / arr.length);
    console.log(zeros / arr.length);
}

function main(){
    plusMinus([1, 1, 0, -1, -1])
}