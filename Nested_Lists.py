# This code is written by harsh.
if __name__ == "__main__":
    n = int(input())
    list1 = []
    list2 = []
    lowest = 1e8
    secondLowest = 1e8
    for i in range(n):
        name = input()
        marks = float(input())
        if marks < lowest:
            secondLowest = lowest
            lowest = marks
        if marks < secondLowest and marks > lowest:
            secondLowest = marks
        list1.append([name, marks])
    for i in range(n):
        if list1[i][1] == secondLowest:
            list2.append(list1[i][0])
    list2.sort()
    for i in range(len(list2)):
        print(list2[i])
