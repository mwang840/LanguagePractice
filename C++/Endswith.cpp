#include <iostream>
#include <string>

bool solution(std::string const &str, std::string const &ending) {
    /*
    Idea:
    grab the last two indexes of the string and compare it with the ending
    If they match, return true, else return false
    (Edit: I decide to add in a comparison between the two strings length)
    */

    if (ending.length() > str.length()) {
        return false;
    }

    std::string lastLetters = str.substr(str.length() - ending.length(), ending.length());
    return lastLetters == ending;
}

int main(){
    std::string word = "abcd";
    std::string end = "cd";
    std::cout << solution(word, end);
    return 0;
}