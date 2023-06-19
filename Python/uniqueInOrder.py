##takes in a sequence of elements and returns a list of only unique characters only while preserving the order
def uniqueInOrder(sequence):
    uniqueOrder = []
    for s in sequence:
        if len(uniqueOrder) < 1 or not s == uniqueOrder[len(uniqueOrder) - 1]:
            uniqueOrder.append(s)
    return uniqueOrder

def main():
    seq = 'AAAABBBCCDAABBB'
    seq1 = 'ABBCcAD'
    seq2 = [1, 2, 2, 3, 3]
    seq3 = (1, 2, 2, 3, 3)
    print(uniqueInOrder(seq))
    print(uniqueInOrder(seq1))
    print(uniqueInOrder(seq2))
    print(uniqueInOrder(seq3))

if __name__ in "__main__":
    main()    