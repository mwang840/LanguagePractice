const isPalindrome = function(x){
    const numToString = x.toString();
    const numToStringReverse = x.toString().split("").reverse().join("");
    return numToString === numToStringReverse;
} ;

function main(){
    const positive = isPalindrome(121);
}

main();