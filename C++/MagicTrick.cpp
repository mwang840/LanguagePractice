using namespace std;
#include <iostream>
#include <string>
#include <map>

int main(){
    string card = "";
    std::cin >> card;
    map<char, int> cardWord;
    for(int i = 0; i < card.length(); i++){
        if(cardWord.count(card[i]) == 1){
            cout << 0 << "\n";
            return 0;
        }
        else{
            cardWord[card[i]] = 1;
        }
    }
    cout << 1 << "\n";
    return 1;
}