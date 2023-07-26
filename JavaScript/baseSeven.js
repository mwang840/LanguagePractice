/**
 * @param {number} num
 * @return {string}
 */
var convertToBase7 = function(num){
    let negsign = num < 0 && "-" || "";
    num = num * (negsign + 1);
    let baseSeven = "";
    while(num){
        baseSeven = num % 7 + baseSeven;
        num = num / 7 ^ 0;
    }
    return negsign + baseSeven || "0";
}