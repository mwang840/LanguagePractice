function createPhoneNumber(numbers){
    
    //Check if the array passed in is a valid phone number, it has to have 10 digits
    if(numbers.length !== 10){
        return undefined;
    }
    else{
        //Slice the list, by the first three numbers, add () around it, and add a dash between the second and final three numbers
        const areaCode = numbers.slice(0, 3)
        const prefix = numbers.slice(3, 6)
        const number = numbers.slice(6)
        return "(" + areaCode.join("") + ") " + prefix.join("") + "-" + number.join("")
    }
  
}

function main(){
    console.log(createPhoneNumber([4,2,0,6,9,5,3,8,1,7]))
}

main()