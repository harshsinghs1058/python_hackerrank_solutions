# This code is written by harsh.
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    for i in range(n):
        if a[i] < a[0]:
            print(a[i])
            break
