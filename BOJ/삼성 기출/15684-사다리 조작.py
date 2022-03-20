n, m, h = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))
graph = []
for _ in range(h):
    graph.append([0] * n)
for i in range(len(arr)):
    a, b = arr[i]
    graph[a - 1][b - 1] = 1

answer = 4


def solution():
    dfs(0, 0, 0)

    return answer


def find():
    for i in range(len(graph[0])):
        k = i
        for j in range(len(graph)):
            if graph[j][k] == 1:
                k += 1
            elif k > 0 and graph[j][k - 1] == 1:
                k -= 1
        if i != k:
            return False
    return True


def dfs(cnt, x, y):
    global answer
    if find():
        answer = min(answer, cnt)
        return
    elif cnt == 3 or cnt >= answer:
        return
    for i in range(x, len(graph)):
        if i == a:
            k = y
        else:
            k = 0
        for j in range(k, len(graph[0]) - 1):
            if not graph[i][j] and not graph[i][j + 1]:
                if j > 0 and graph[i][j - 1]:
                    continue
                graph[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                graph[i][j] = 0


result = solution()
if result >= 4:
    result = -1
print(result)
