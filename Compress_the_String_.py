# This code is written by harsh.
if __name__ == "__main__":
    s = input()
    temp = 0
    for i in range(len(s)):
        if s[i] == s[i - 1]:
            temp += 1
        elif temp != 0:
            print(f"({temp}, {s[i - 1]})", end=" ")
            temp = 1
        else:
            temp += 1
    print(f"({temp}, {s[len(s) - 1]})", end=" ")
