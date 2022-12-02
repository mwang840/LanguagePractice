#include <bits/stdc++.h>
#include <vector>


int main(){
    int testCase = 0;
    std::cin>>testCase;
    int deers[4] = {0, 0, 0, 0};
    for(int i = 0; i < testCase; i++){
        int rudolph, deer1, deer2, deer3 = 0;
        std::cin>> rudolph >> deer1 >> deer2 >> deer3;
        deers[0] = rudolph;
        deers[1] = deer1;
        deers[2] = deer2;
        deers[3] = deer3;
        int howManyRenideer = 0;
        int rudolphDis = deers[0];
        for(int i = 1; i < 4; i++){
            if(rudolphDis < deers[i]){
                howManyRenideer++;
        }
    }
    std::cout << howManyRenideer << "\n";
    }
    
        
}