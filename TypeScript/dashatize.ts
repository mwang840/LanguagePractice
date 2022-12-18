export const dashatize = (num: number)=>{
    //Check to see if n is a number
    if(isNaN(num)){
        return "NaN";
    }
    else{
        //One replace method
        //Turns the num to a string, uses regex to check if every digit is a odd digit, then adds the dashes on both sides
        //if there are multiple dashes, replace it with one dashatize
        //if the dash is at the beginning, remove it
        //if the dash is at the end, remove it
        return num.toString().replace(/([13579])/g, '-$1-').replace(/\-+/g, "-").replace(/^\-/, '').replace(/\-$/,'');
    }
};
console.log(dashatize(1))
console.log(dashatize(274));
console.log(dashatize(6815));