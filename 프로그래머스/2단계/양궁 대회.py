temp = []
answer = [0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def solution(n, info):
    global answer
    dfs(0, n, info)
    if answer[0] == 0:
        return [-1]
    else:
        return answer[1]


def dfs(a, n, info):
    if len(temp) == n:
        check(temp, info)
        return
    for i in range(a, 11):
        temp.append(i)
        dfs(i, n, info)
        temp.pop()


def check(temp, info):
    print(temp)
    global answer
    a = 0
    b = 0
    arr = [0] * 11
    for i in temp:
        arr[10 - i] += 1
    for i in range(len(info)):
        if info[i] < arr[i]:
            b += 10 - i
        else:
            if info[i] != 0:
                a += 10 - i
    if answer[0] < b - a:
        answer[1] = arr
        answer[0] = b - a
    if answer[0] == b - a:
        for i in range(10, -1, -1):
            if arr[i] > answer[1][i]:
                answer[1] = arr
                break
            if arr[i] < answer[1][i]:
                break
