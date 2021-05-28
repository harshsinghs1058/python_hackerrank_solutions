# This code is written by harsh.
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print((" " * (n - i - 1)), end="")
        print("H" * (2 * i + 1))
    for i in range(n + 1):
        print(" " * (n // 2), end="")
        print("H" * n, end="")
        print(" " * (3 * n), end="")
        print("H" * n)
    for i in range((n // 2) + 1):
        print(" " * (n // 2), end="")
        print("H" * 5 * n)
    for i in range(n + 1):
        print(" " * (n // 2), end="")
        print("H" * n, end="")
        print(" " * (3 * n), end="")
        print("H" * n)
    for i in range(n):
        print(" " * (4 * n + i), end="")
        print("H" * ((2 * (n - i)) - 1))
