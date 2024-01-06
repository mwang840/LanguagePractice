function convertFrac(lst){
    //Your code here
    //First step is to grab the least common denominator
    let denominators = lst.map(x=>x[1]);
    //find lcm of the denominator
    let commonMultiple = calcLcm(denominators);
    const updatedDenom = (denom) => denom = commonMultiple;
    let newDenominators = denominators.map(updatedDenom);
    let newNumerators = denominators.map(numerator=> commonMultiple / numerator)
    const fractOfTuples = newNumerators.map((value, index) => [value, newDenominators[index]]);
    const strTuple = fractOfTuples.map(tuple => `(${tuple.join(',')})`).join('');
    return strTuple;
}

function calcLcm(nums){
    if(nums.length < 2){
        return 0;
    }

    let result = nums[0];
    for (let i = 1; i < nums.length; i++) {
        result = lcm(result, nums[i]);
    }

    return result;
}
//Calculates the greatest common demonimator of the two
function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}

// Function to find the least common multiple (LCM) of two numbers
function lcm(a, b) {
    return (a * b) / gcd(a, b);
}

function main(){
    var lst = [ [1, 2], [1, 3], [1, 4] ];
    console.log(convertFrac(lst));
    var lst2 = [[1, 5], [1,6]];
    console.log((convertFrac(lst2)))
}

main()