export const dashatize = (num: number)=>{
    //Check to see if n is a number
    if(isNaN(num)){
        return "NaN";
    }
    //Negative Nums should be positive integers 
    //Converts the number to a string array
    const toString = Math.abs(num).toString();
    let result = toString.split('');
    let answer:string[] = [];
    //console.log("Answer equals ", answer);
    //console.log(result);
    //Set up length
    const length = toString.length;
    //We will loop over the string and check to see if its odd and positions
    for(let i = 0; i < length; i++){
        //Check to see if we are AT the front of the string
        //Checks to see if its indexes is even then add the dashes
        if(i > 0 && Number(toString[i - 1]) % 2 == 0){
            answer.push(`-${result[i]}`);
        }
        else if(i < length - 1 && Number(toString[i + 1]) % 2 == 0){
            answer.push(`${result[i]}`);
        }
        else if(i > 0 && Number(toString[i - 1]) % 2 == 1){
            answer.push(`-${result[i]}`);
        }
        else{
            answer.push(`${result[i]}`);
        }
    }
    //checks if we are at the left end
    //console.log(answer);
    return answer.join("");
};
console.log(dashatize(1))
console.log(dashatize(274));
console.log(dashatize(6815));