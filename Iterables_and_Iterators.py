# This code is written by harsh.
from itertools import combinations

if __name__ == "__main__":
    n = int(input())
    ans = 0
    a = list(map(str, input().split()))
    m = int(input())
    list1 = list(combinations(a, m))
    for i in list1:
        if "a" in i:
            ans += 1
    print((ans / len(list1)))
