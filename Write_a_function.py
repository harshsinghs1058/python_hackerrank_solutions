# This code is written by harsh.
def is_leap(n):
    leap = False
    if n % 4 == 0:
        leap = True
        if n % 100 == 0:
            leap = False
            if n % 400 == 0:
                leap = True
    return leap


if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))
