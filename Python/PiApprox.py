from math import pi
def iter_pi(epsilon):
    approx = 0
    oddOne = 1
    sign = 1
    i = 0

    while abs(approx * 4 - pi) > epsilon:
        approx += 1.0 / (oddOne * sign)
        oddOne += 2
        sign *=-1
        i+=1
    return [i, round(approx * 4, 10)]



def main():
    print(iter_pi(0.1))
    print(iter_pi(0.01))
    print(iter_pi(0.001))


if __name__  == "__main__":
    main()   