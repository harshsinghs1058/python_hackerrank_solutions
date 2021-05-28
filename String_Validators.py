# This code is written by harsh.
if __name__ == "__main__":
    s = input()
    alphabte = False
    num = False
    upper = False
    lower = False
    for i in range(len(s)):
        if s[i].isalpha():
            alphabte = True
        if s[i].isnumeric():
            num = True
        if s[i].isupper():
            upper = True
        if s[i].islower():
            lower = True
    if alphabte or num:
        print(True)
    else:
        print(False)
    print(alphabte)
    print(num)
    print(lower)
    print(upper)
