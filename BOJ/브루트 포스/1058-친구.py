n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
arr = [0] * n


def solution():
    global arr
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == 'Y':
                arr[i] += 1
            else:
                a = check(i, j)
                arr[i] += a
    return max(arr)


def check(a, b):
    cnt = 0
    for i in range(n):
        if graph[i][a] == 'Y' and graph[i][b] == 'Y':
            cnt = 1
    return cnt


print(solution())
