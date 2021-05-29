# This code is written by harsh.
if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    for _ in range(int(input())):
        queue = input()
        if queue.startswith("pop"):
            s.pop()
        elif queue.startswith("remove"):
            temp, a = queue.split()
            a = int(a)
            s.remove(a)
        elif queue.startswith("discard"):
            temp, a = queue.split()
            a = int(a)
            s.discard(a)
    print(sum(s))
