# this code is written by harsh
import textwrap


def wrap(string, max_width):
    temp = textwrap.wrap(string, max_width)
    ans = ""
    for i in range(len(temp)):
        ans += temp[i] + "\n"
    return ans


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
