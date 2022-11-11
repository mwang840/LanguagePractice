#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *to_jaden_case(char *jaden_case, const char *string);


int main(){
    char *sentence = (malloc(sizeof(char)));
    char *correctSentence = (malloc(sizeof(char)));
    scanf("Enter an sentence %s", &sentence);
    scanf("Enter a correct grammatical sentence %s", &correctSentence);
    printf("Jaiden case of this sentence is %s", to_jaden_case(sentence, correctSentence));
    return 0;
}

char *to_jaden_case(char *jaden_case, const char *string){
    int i = 0;
    char *toJaiden = jaden_case;
    if(string[i] >= 'a' && string[i] <= 'z'){
        toJaiden[i] = string[i]  - 32;
        i++;
    }
    while(string[i] != '\0'){
        if(string[i] == ' '){
            toJaiden[i] = string[i];
            i++;
            toJaiden[i] = string[i] - 32;
        }
        else{
            toJaiden[i] = string[i];
        }
        i++;
    }
    toJaiden[i] = '\0';
    return toJaiden;
}