def max_sequence(arr):
    length = len(arr)
    if length == 0:
        return 0
    elif all(element < 0 for element in arr):
        return 0
    maxSum = -99999999999999
    currentSum = 0
    for a in arr:
        currentSum = max(a, a + currentSum)
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum

def main():
    sequence = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sequence(sequence))

main()
