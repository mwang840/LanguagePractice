using namespace std;
#include <iostream>
#include <string>
#include <map>
class RGBToHex
{
  public:
  static std::string rgb(int r, int g, int b);
  //Adding helper functions
  static std::string torgbVal(int value);  
  static std::string convertToHex(int rgbValue); 
};


string RGBToHex::rgb(int r, int g, int b){
    return torgbVal(r) + torgbVal(g) + torgbVal(b);
}

//Converts the function to an rgbvalue first with the integer
string RGBToHex::torgbVal(int value){
    //Edge cases if the value is equal to zero or less than zero or greater then 255
    if(value <= 0){
        return "00";
    }else if(value >= 255){
        return "FF";
    }
    //Other wise we divide the value by 16 for the first value
    //And find the remainder as well if the number is not divisible by 16
    int hexVal1 = value / 16;
    int hexVal2 = ((value / 16) - hexVal1) * 16;
    return convertToHex(hexVal1) + convertToHex(hexVal2);
}

//Converts the existing rgb value to an Hexvalue, grabs the value out of the map
string RGBToHex::convertToHex(int rgbValue){
    map<int, string> rgbvals;
    rgbvals[0] = "0";
    rgbvals[1] = "1";
    rgbvals[2] = "2";
    rgbvals[3] = "3";
    rgbvals[4] = "4";
    rgbvals[5] = "5";
    rgbvals[6] = "6";
    rgbvals[7] = "7";
    rgbvals[8] = "8";
    rgbvals[9] = "9";
    rgbvals[10] = "A";
    rgbvals[11] = "B";
    rgbvals[12] = "C";
    rgbvals[13] = "D";
    rgbvals[14] = "E";
    rgbvals[15] = "F";
    return rgbvals[rgbValue];
}



int main(){
    RGBToHex red, black, blue, green, yellow;
    std::cout << red.rgb(255, 255, 255) << "\n";
    std::cout << black.rgb(0, 0, 0) << "\n";
    std::cout << blue.rgb(1, 2, 3) << "\n";
    return 0;
}
