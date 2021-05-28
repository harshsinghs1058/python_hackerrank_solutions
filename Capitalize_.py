# This code is written by harsh.
def solve(s):
    ans = s[0].upper()
    for i in range(1, len(s)):
        if s[i - 1] == " ":
            ans += s[i].upper()
        else:
            ans += s[i]
    return ans


if __name__ == "__main__":
    s = input()
    print(solve(s))
