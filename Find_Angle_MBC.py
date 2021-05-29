# This code is written by harsh.
from math import *

if __name__ == "__main__":
    ab = int(input())
    bc = int(input())
    angleC = atan((ab / bc))
    ans = round(angleC * 57.2958)
    if bc >= ab:
        print(min(ans, 90 - ans), end="")
    else:
        print(max(ans, 90 - ans), end="")
    print(u"\xb0")
