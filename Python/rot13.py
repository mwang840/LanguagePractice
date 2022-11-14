def rot13(message):
    cypher = ""
    for mess in message:
        currMessage = ord(mess)
        if(currMessage >= 97 and currMessage < 123):
            currMessage = ((currMessage  - 84) % 26) + 97
        elif(currMessage >= 65 and currMessage <91):
            currMessage  = ((currMessage - 52) % 26) + 65  
        cypher += chr(currMessage)
    return cypher

def main():
    word = str(input("Enter a message"))
    print("Word inputted in is: ", word)
    print("Rot13 version of the word is: ", rot13(word))


if __name__  == "__main__":
    main()   