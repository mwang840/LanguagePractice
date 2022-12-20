function sexy_prime(x, y){
    if(x < 2 || y < 2) return false
  
    function prime(n){
      for(var i=2;i<n;i++){
        if(n % i == 0) return false
      }
      return true
    }
  
    var arr = []
    for(var i=x;i<y;i++){
        if(prime(i)) arr.push(i)
    }
    
    if(!prime(x)||!prime(y)) return false
    else if(x + 6 == y || y + 6 == x){
      return true
    }
    return false
  }