# This code is written by harsh.
from itertools import permutations

if __name__ == "__main__":
    s, n = input().split()
    n = int(n)
    list1 = list(permutations(s, n))
    list1.sort()
    for item in list1:
        for k in item:
            print(k, end="")
        print()
