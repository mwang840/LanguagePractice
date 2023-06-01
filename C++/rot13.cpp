#include <string>
#include <iostream>
#include <map>
using namespace std;

string rot13(string msg);

int main()
{
    cout << rot13("abcd") << endl;
    cout << rot13("test") << endl;
    cout << rot13("Test") << endl;
    return 0;
}

string rot13(string msg)
{
    string cipherR13 = "";
    for (int i = 0; i < msg.length(); i++)
    {
        char currentChar = msg.at(i);
        if (currentChar >= 'a' && currentChar <= 'm')
        {
            currentChar += 13;
        }
        else if (currentChar >= 'A' && currentChar <= 'M')
        {
            currentChar += 13;
        }
        else if (currentChar >= 'm' && currentChar <= 'z')
        {
            currentChar -= 13;
        }
        else if (currentChar >= 'M' && currentChar <= 'Z')
        {
            currentChar -= 13;
        }
        cipherR13 += currentChar;
    }
    return cipherR13;
}