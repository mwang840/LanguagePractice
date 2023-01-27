def vaporCode(s: str) -> str:
    return '  '.join(letter.upper() for letter in s if letter != '  ')



def main():
    print(vaporCode("Lets go to the movies"))
    print(vaporCode("Why isn't my code working?"))

if __name__ == "__main__":
    main()    