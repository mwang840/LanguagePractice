function convertFrac(lst){
    //Your code here
    //First step is to grab the least common denominator
     const cd = lst.reduce((a, [_, d]) => lcm(d, a), 1);
    return lst.map(([n, d]) => `(${n * cd/d},${cd})`).join('');
}

//Calculates the greatest common demonimator of the two
function gcd(a, b) {
    return b ? gcd(b, a % b) : a;
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