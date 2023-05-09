
def handy(amount: int)->int:
    count = 0
    if amount == 0:
        count += 1
    while amount != 0:
        amount //= 10
        count += 1
    return count    


def main():
    testCase = int(input())
    for test in range(testCase):
        result = int(input())
        print(handy(result))

if __name__ in "__main__":
    main()        