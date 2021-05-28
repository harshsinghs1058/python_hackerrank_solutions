# This code is written by harsh.
def c(temp):
    return chr(temp + 96)


def print_rangoli(n):
    # print(c(n).center((4 * n - 2), "-"))
    for i in range(n):
        print("-" * (n - i - 1) * 2, end=c(n))
        # print(c(n), end="")
        for j in range(i):
            print("-", end="")
            print(c(n - j - 1), end="")
        for j in range(i, 0, -1):
            print("-", end="")
            print(c(n - j + 1), end="")
        print("-" * (n - i - 1) * 2)
    for i in range(n - 1):
        print("-" * (i + 1) * 2, end=c(n))
        for j in range(n - 1, i + 1, -1):
            print("-", end="")
            print(c(j), end="")
        for j in range(i, n - 2):
            print("-", end="")
            print(c(j + 3), end="")
        print("-" * (i + 1) * 2)


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
