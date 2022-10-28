#include <iostream>
#include <math.h>
using namespace std;


int main(){
    int cases = 0;
    int floor = 0;
    std::cin >> cases;
    //given two apartments on the first floor
    for(int i = 0; i < cases; i++){
        int apartment, petyasApartment = 0;
        cin >> apartment >> petyasApartment;
        if(apartment == 1 || apartment == 2){
            floor = 1;
        }
        else{
           floor = int(ceil((apartment - 2)/petyasApartment)) + 1;
        }
        int actualFloor = floor;
        std::cout << "Floor number is: " << floor;   
    }
     
    return 0;
}