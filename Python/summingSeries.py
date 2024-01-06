import math
def summingSeries(n):
    if n % 2 == 0:
        return (n // 2) * ((n // 2) + 1)
    # If n is odd, the sum is (n+1)/2 * (n+1)/2 - this is the sum of the first (n+1)/2 positive odd numbers.
    else:
        return ((n + 1) // 2) ** 2


def main():
    sequence = 2
    print(summingSeries(sequence))


if __name__ in "__main__":
    main()