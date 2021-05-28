# This code is written by harsh.
def minion_game(s):
    n = len(s)
    Kevin = 0
    Stuart = 0
    for i in range(n):
        if s[i] in "AEIOU":
            Kevin += n - i
        else:
            Stuart += n - i
    if Stuart == Kevin:
        print("Draw")
    elif Stuart > Kevin:
        print("Stuart", Stuart)
    else:
        print("Kevin", Kevin)


if __name__ == "__main__":
    s = input()
    minion_game(s)
