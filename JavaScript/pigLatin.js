function pigIt(str){
    //convert existing string to an array via splitting by whitespace
    const strArray = str.split(" ");
    const Ayye = "ay";
    //Grab the first character of each element (store it in a variable and attach it to the end of each element followed by a "ay")
    let firstChar = '';
    for(let i = 0; i < strArray.length; i++){
        //Check to see if any puncuation does not exist in the array.
        if(!!strArray[i].match(/^[.,:!?]/) === false){
            firstChar = strArray[i].charAt(0);
            strArray[i] = strArray[i].slice(1);
            strArray[i] += firstChar + Ayye;
        }   
    }
    //convert array back to string and strip commas
    return strArray.toString().replaceAll(",", " ");
}

function main(){
    const pigLatin = console.log(pigIt("Pig latin is cool"));
}

main();