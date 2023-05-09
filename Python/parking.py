def main():
    testCase = int(input())

    for i in range(testCase):
        n = int(input())
        stores = input().split()
        for k in range(n):
            stores[k] = int(stores[k])
        stores.sort()
        print((max(stores) - min(stores)) * 2)        

if __name__ in "__main__":
    main()    