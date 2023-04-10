#include <iostream>
using namespace std;

int climbStairs(int n);
int fib(int n);
int main(){
    int stairs = 45;
    std:: cout << climbStairs(stairs) << "\n";
    return 0;
}

int climbStairs(int n){

    return fib(n + 1);

}

int fib(int n){
    if(n<= 1){
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

