package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(sexy_prime(5, 11))
	fmt.Println(sexy_prime(13, 19))
	fmt.Println(sexy_prime(83, 89))
	fmt.Println(sexy_prime(1, 11))
}

func sexy_prime(x int, y int) bool {
	if isPrime(x) == false || isPrime(y) == false {
		return false
	} else if isPrime(x) == true && isPrime(y) == true {
		if y-x == 6 {
			return true
		} else if y-x != 6 {
			return false
		}
	}
	return false
}

func isPrime(n int) bool {
	//Edge case if n is either zero or negative
	if n <= 0 {
		return false
	} else if n == 1 {
		return false
	} else {
		for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
			if n%i == 0 {
				return false
			}
		}
		return true
	}
}
