temp = []
answer = 0


def solution(expression):
    temp = []
    arr = []
    arr2 = []
    for i in expression:
        if i.isdigit():
            temp.append(i)
        else:
            arr.append(int(''.join(temp)))
            arr.append(i)
            arr2.append(i)
            temp = []
    arr.append(int(''.join(temp)))
    arr2 = set(arr2)
    arr2 = list(arr2)
    visited = [0] * len(arr2)
    dfs(arr2, visited, arr)

    return answer


def dfs(arr2, visited, arr):
    if len(temp) == len(visited):
        check(temp, arr)
        return
    for i in range(len(arr2)):
        if visited[i] == 0:
            visited[i] = 1
            temp.append(arr2[i])
            dfs(arr2, visited, arr)
            temp.pop()
            visited[i] = 0


def check(temp, arr):
    global answer
    value = []
    value2 = []
    for i in temp:
        for j in range(len(arr)):
            value.append(arr[j])
            if len(value) == 3:
                if value[1] == i:
                    if i == '-':
                        k = value[0] - value[2]
                    if i == '+':
                        k = value[0] + value[2]
                    if i == '*':
                        k = value[0] * value[2]
                    value = []
                    value.append(k)
                else:
                    for p in range(2):
                        value2.append(value[p])
                    value = [value[2]]
        value2.append(value[-1])
        arr = value2
        value = []
        value2 = []
    answer = max(answer, abs(arr[0]))
