def addBinary(self, a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)
    return format((a + b), "b")

def main():
    first = "11"
    second = "1"
    print(addBinary(first, second))


if __name__ in "__main__":
    main()