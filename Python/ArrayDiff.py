def array_diff(a: list[int], b: list[int]):
    final_list = [first for first in a if first not in b]
    return final_list


def main():
    first = [1, 2, 3]
    second = [1, 2]
    print(array_diff(first, second))


if __name__ in "__main__":
    main()