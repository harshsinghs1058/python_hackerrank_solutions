# This code is written by harsh.
if __name__ == "__main__":
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    c = a.symmetric_difference(b)
    c = list(c)
    c.sort()
    for i in c:
        print(i)
