# This code is written by harsh.
from itertools import product

if __name__ == "__main__":
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    list3 = list(product(list1, list2))
    for item in list3:
        print(item, end=" ")
