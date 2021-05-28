# this code is written by harsh
def count_substring(string, sub_string):
    ans = 0
    for i in range(len(string)):
        if len(string[i : len(sub_string) + i]) != len(sub_string):
            break
        if sub_string == string[i : len(sub_string) + i]:
            ans = ans + 1
    return ans


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
