import copy

n, m, h = map(int, input().split())
graph = []
for _ in range(h):
    graph.append([0] * n)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
temp = []
answer = 4


def solution():
    if m == 0:
        return 0
    for i in range(4):
        dfs(0, i)
    if answer == 1e9:
        return -1
    else:
        return answer


def dfs(a, l):
    if len(temp) > answer:
        return
    if len(temp) == l:
        check(temp, l)
        return
    for i in range(a, h):
        for j in range(n - 1):
            if graph[i][j] == 0:
                if temp:
                    if j > 0 and temp[-1][0] == i and temp[-1][1] == j - 1:
                        continue
                    else:
                        if (j > 0 and graph[i][j - 1] == 1) or graph[i][j + 1] == 1:
                            continue
                        else:
                            temp.append([i, j])
                            dfs(i + 1, l)
                            temp.pop()
                else:
                    if (j > 0 and graph[i][j - 1] == 1) or graph[i][j + 1] == 1:
                        continue
                    else:
                        temp.append([i, j])
                        dfs(i + 1, l)
                        temp.pop()


def check(temp, l):
    global answer
    cnt = 0
    visited = copy.deepcopy(graph)
    for i in range(len(temp)):
        x, y = temp[i]
        visited[x][y] = 1
    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    for i in range(n):
        x = 0
        y = i
        while True:
            if visited[x][y] == 1:
                d = 1
                x += dx[d]
                y += dy[d]
                d = 2
                x += dx[d]
                y += dy[d]
            elif y >= 1:
                if visited[x][y - 1] == 1:
                    d = 0
                    x += dx[d]
                    y += dy[d]
                    d = 2
                    x += dx[d]
                    y += dy[d]
                else:
                    d = 2
                    x += dx[d]
                    y += dy[d]
            else:
                d = 2
                x += dx[d]
                y += dy[d]
            if x == h:
                if y == i:
                    cnt += 1
                    break
                else:
                    break
    if cnt == n:
        answer = min(answer, l)


print(solution())
