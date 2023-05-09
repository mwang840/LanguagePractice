def main():
    testCases = int(input())
    for test in range(testCases):
        candies = input()
        children = int(input())
        sumOfCandies = 0
        for child in range(children):
            howManyCandies = int(input())
            sumOfCandies += howManyCandies
        status = 'YES' if (sumOfCandies%children==0) else 'NO'
        print(status)  

if __name__ in "__main__":
    main()            