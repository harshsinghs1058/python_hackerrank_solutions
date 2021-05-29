# This code is written by harsh.
def uidCheck(s):
    upper = 0
    digits = 0
    if len(s) != 10:
        return False
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    for i in range(len(s)):
        if not s[i].isalnum():
            return False
        if s[i].isdigit():
            digits += 1

        if s[i].isupper():
            upper += 1
    if upper < 2 or digits < 3:
        return False
    return True


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        uid = input()
        if uidCheck(uid):
            print("Valid")
        else:
            print("Invalid")
