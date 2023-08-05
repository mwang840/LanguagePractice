const handshake = function(n){
    //case if the person is by him/herself
    if(n == 1){
        return 0;
    }
    if(n == 2){
        return 1;
    }
    else if(n > 2){
        return shakeHandsMorethanOnePerson(n)
    }
    
}


const shakeHandsMorethanOnePerson = function(n){
    const possibleHandshakes = (n * (n - 1)) / 2;
    return possibleHandshakes
}

const main = function main(){
    console.log(handshake(5))
}

main()
