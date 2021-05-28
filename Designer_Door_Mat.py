# This code is written by harsh.
if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(n // 2):
        print("-" * ((m // 2 - 3 * i) - 1), end="")
        print(".|", end="")
        print("..|" * 2 * i, end="")
        print(".", end="")
        print("-" * ((m // 2 - 3 * i) - 1))
    print("WELCOME".center(m, "-"))
    for i in range(n // 2 - 1, -1, -1):
        print("-" * ((m // 2 - 3 * i) - 1), end="")
        print(".|", end="")
        print("..|" * 2 * i, end="")
        print(".", end="")
        print("-" * ((m // 2 - 3 * i) - 1))
