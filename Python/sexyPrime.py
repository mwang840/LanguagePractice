def sexy_prime(x, y):
    sexy = False
    if isPrime(x) == False or isPrime(y) == False:
        return False
    elif isPrime(x) == True and isPrime(y) == True:
        if y - x == 6 or x + 6 == y or y+6 == x:
            sexy = True
        elif y - x != 6:
            sexy = False
    return sexy


def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True