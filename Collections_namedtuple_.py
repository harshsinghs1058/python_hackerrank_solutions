# This code is written by harsh.
from collections import namedtuple

if __name__ == "__main__":
    n = int(input())
    fields = input()
    s = namedtuple("s", fields)
    totalMarks = 0
    for i in range(n):
        temp = s(*input().split())
        totalMarks += int(temp.MARKS)
    print(totalMarks / n)
