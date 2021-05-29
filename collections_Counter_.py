# This code is written by harsh.
from collections import Counter

if __name__ == "__main__":
    n = int(input())
    shoes = list(map(int, input().split()))
    m = int(input())
    shoeCollection = Counter(shoes)
    ans = 0
    for i in range(m):
        size, amount = map(int, input().split())
        if shoeCollection[size] > 0:
            ans += amount
            shoeCollection[size] -= 1
    print(ans)
