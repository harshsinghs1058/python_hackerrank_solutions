# This code is written by harsh.
from itertools import combinations

if __name__ == "__main__":
    s, n = input().split()
    n = int(n)
    imp = []
    for i in range(n):
        list1 = list(combinations(s, i + 1))
        for item in list1:
            item = list(item)
            item.sort()
            temp = ""
            for i in item:
                temp += i
            imp.append(temp)
    imp.sort()
    for i in range(n):
        for item in imp:
            if len(item) == i + 1:
                print(item)
