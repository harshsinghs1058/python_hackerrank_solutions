# This code is written by harsh.
from itertools import combinations_with_replacement

if __name__ == "__main__":
    s, n = input().split()
    n = int(n)
    list1 = list(combinations_with_replacement(s, n))
    ans = []
    for i in list1:
        temp = ""
        i = list(i)
        i.sort()
        for k in i:
            temp += k
        ans.append(temp)
    ans.sort()
    for i in ans:
        print(i)
