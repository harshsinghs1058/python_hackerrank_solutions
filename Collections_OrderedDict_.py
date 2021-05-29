# This code is written by harsh.
from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    d = OrderedDict()
    for _ in range(n):
        *t1, t2 = input().split()
        t2 = int(t2)
        s = " ".join(t1)
        if s in d.keys():
            temp = d[s]
            d[s] = temp + t2
        else:
            d[s] = t2
    for i, k in d.items():
        print(i, k)
