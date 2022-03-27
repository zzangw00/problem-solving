r, c, k = map(int, input().split())
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))


def solution():
    answer = 0
    if r <= len(arr) and c <= len(arr[0]):
        if arr[r - 1][c - 1] == k:
            return answer

    while True:
        if answer == 101:
            answer = -1
            return answer
        if len(arr) >= len(arr[0]):
            rCal()
            answer += 1
        else:
            cCal()
            answer += 1
        if r - 1 < len(arr) and c - 1 < len(arr[0]):
            if arr[r - 1][c - 1] == k:
                return answer


def rCal():
    global arr
    a = 0
    for x in range(len(arr)):
        temp = [0] * 101
        temp2 = []
        temp3 = []
        for y in range(len(arr[x])):
            temp[arr[x][y]] += 1
        for i in range(1, len(temp)):
            if temp[i] != 0:
                temp2.append([i, temp[i]])
        temp2.sort(key=lambda x: (x[1], x[0]))
        for i in range(len(temp2)):
            for j in range(2):
                temp3.append(temp2[i][j])
        a = max(a, len(temp3))
        arr[x] = temp3
    for x in range(len(arr)):
        if len(arr[x]) != a:
            for y in range(a - len(arr[x])):
                arr[x].append(0)


def cCal():
    global arr
    a = 0
    arr1 = []
    for y in range(len(arr[0])):
        temp = [0] * 101
        temp2 = []
        temp3 = []
        for x in range(len(arr)):
            temp[arr[x][y]] += 1
        for i in range(1, len(temp)):
            if temp[i] != 0:
                temp2.append([i, temp[i]])
        temp2.sort(key=lambda x: (x[1], x[0]))
        for i in range(len(temp2)):
            for j in range(2):
                temp3.append(temp2[i][j])
        a = max(a, len(temp3))
        arr1.append(temp3)
    for i in range(len(arr1)):
        temp4 = []
        if len(arr1[i]) != a:
            for j in range(a - len(arr1[i])):
                temp4.append(0)
        arr1[i] = arr1[i] + temp4
    arr2 = []
    for i in range(len(arr1[0])):
        arr2.append([0] * len(arr1))
    for x in range(len(arr1)):
        for y in range(len(arr1[0])):
            arr2[y][x] = arr1[x][y]
    arr = arr2


print(solution())