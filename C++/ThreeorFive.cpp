#include <iostream>


bool multipleOfThree(int num);
bool multipleOfFive(int num);

bool multipleOfThree(int num){
    return num % 3 == 0;
}

bool multipleOfFive(int num){
    return num % 5 == 0;
}


int solution(int number) 
{
    /*
    Is it worth to loop from 0 to n?
    Well that depends on how big n is
    Is there a way to not forget about a loop when counting numbers less than n?
    Also do a negative number check
    */

    int result = 0;

    for(int i = 0; i < number; i++){
        if(multipleOfThree(i) == true || multipleOfFive(i) == true){
            result+=i;
        }
    }

    return result;
}


int main(){

    std::cout << solution(11);
    return 0;
}