# This code is written by harsh.
if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range(n):
        query = input()
        if query.startswith("print"):
            print(a)
        elif query.startswith("pop"):
            a.pop()
        elif query.startswith("reverse"):
            a.reverse()
        elif query.startswith("sort"):
            a.sort()
        elif query.startswith("append"):
            temp, temp2 = query.split()
            num = int(temp2)
            a.append(num)

        elif query.startswith("remove"):
            temp, temp2 = query.split()
            num = int(temp2)
            a.remove(num)
        elif query.startswith("insert"):
            temp, temp2, temp3 = query.split()
            pos = int(temp2)
            num = int(temp3)
            a.insert(pos, num)
