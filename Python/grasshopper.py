def main():
    ##Read in input first
    ##Read in the input and the endcase
    ##have a variable that stores the numbers which are not divisible by k
    testCases = int(input())
    for test in range(testCases):
        number, constraint = [int(x) for x in input().split()]  
        nonDivisible = 0
        jumps = []
        for num in range(number):
            if num % constraint != 0:
                nonDivisible += 1
        jumps.append(nonDivisible)
        jumps.append(number - nonDivisible)
        print(len(jumps))
        print(nonDivisible, end=" ")
        print(number - nonDivisible)


main()