#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>


int getDigitCt(int num);
/** 
 * A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
*/
bool narcissistic(int num)
{
    int power = getDigitCt(num);
    int temporary = num;
    int sum = 0;
    while(temporary > 0){
        int digit = temporary % 10; 
        temporary /=10;
        sum += pow(digit, power);
    }

    return num == sum;
}

/**
 * @brief Get the Number of digits in a given number
 * 
 * @param num 
 * @return int 
 */
int getDigitCt(int num){
   int temporary = num;
   int count = 0;
   while(temporary != 0){
    count++;
    temporary /=10;
   }
   return count;
}

// void splitDigits(int num){
//     int count = 0;
//     int numOfdigits[10];

//     int temporary = num;

//     while(temporary > 0){
//         temporary /= 10;
//         count++;
//     }
//     temporary = num;
//     for (int i = count - 1; i >= 0; i--) {
//         numOfdigits[i] = temporary % 10;
//         temporary /= 10;
//     }
// }

int main(){
    int demoNum = 153;
    narcissistic(demoNum);
    return 0;
}