# This code is written by harsh.
from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    a1 = defaultdict(list)
    for i in range(n):
        temp = input()
        a1[temp].append(i + 1)
    for i in range(m):
        temp = input()
        if len(a1[temp]) > 0:
            for item in a1[temp]:
                print(item, end=" ")
            print()
        else:
            print(-1)
