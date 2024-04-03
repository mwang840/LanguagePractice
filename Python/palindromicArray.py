# Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.
def PalinArray(arr ,n):
    for a in arr:
        string = str(a)
        currentLength = len(string)
        for i in range(currentLength):
            if string[i] !=string[i - 1]:
                return 0
    return 1


def main():
    input = [111, 222, 333, 444, 555]
    elements = 5
    print(PalinArray(input, elements))

if __name__ in "__main__":
    main()