# This code is written by harsh.
if __name__ == "__main__":
    marks = {}
    for _ in range(int(input())):
        name, *temp = input().split()
        marks[name] = list(map(float, temp))
    query_marks = marks[input()]
    ans = sum(query_marks) / len(query_marks)
    print("{0:.2f}".format(ans))
