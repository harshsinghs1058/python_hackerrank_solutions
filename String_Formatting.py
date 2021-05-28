# This code is written by harsh.
def print_formatted(n):
    l_bin = len(str(bin(n))[2:])
    for i in range(1, n + 1):
        print(str(i).rjust(l_bin, " "), end=" ")
        print(str(oct(i))[2:].rjust(l_bin, " "), end=" ")
        print(str(hex(i))[2:].upper().rjust(l_bin, " "), end=" ")
        print(str(bin(i))[2:].upper().rjust(l_bin, " "))


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
