#include <stdio.h>
#include <ctype.h>
#include <iostream>
using namespace std;

string Yes(string s);

int main(){
    int testCases = 0;
    string word = "";
    cin >> testCases;
    cout << "\n";
    for(int i = 0; i < testCases; ++i){
        cin >> word;
        cout<<(Yes(word));
    }
    return 0;
}

string Yes(string s){
    string lower = "";
    for(int i = 0; i < s.length(); ++i){
        lower += tolower(s[i]);
    }
    if(lower == "yes"){
        return "YES\n";
    }
    else{
        return "NO\n";
    }
}