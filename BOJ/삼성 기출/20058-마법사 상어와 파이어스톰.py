from collections import deque
import copy

n, q = map(int, input().split())
graph = []
for _ in range(2 ** n):
    graph.append(list(map(int, input().split())))
arr = list(map(int, input().split()))
temp = []
for _ in range(2 ** n):
    temp.append([0] * (2 ** n))
answer = 0
answer2 = 0
visited = []
for _ in range(2 ** n):
    visited.append([0] * (2 ** n))


def solution():
    for i in arr:
        l = 2 ** i
        for x in range(0, 2 ** n, l):
            for y in range(0, 2 ** n, l):
                cycle(x, y, l)
        checkIce()
    sumIce()
    for x in range(2 ** n):
        for y in range(2 ** n):
            if visited[x][y] == 0 and graph[x][y] != 0:
                visited[x][y] = 1
                bfs(x, y)


def cycle(x, y, l):
    global graph
    temp = deque([])
    for i in range(x, x + l):
        for j in range(y, y + l):
            temp.append(graph[i][j])
    for i in range(y + l - 1, y - 1, -1):
        for j in range(x, x + l):
            graph[j][i] = temp.popleft()


def checkIce():
    global graph
    ice = copy.deepcopy(temp)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(2 ** n):
        for y in range(2 ** n):
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 2 ** n or nx < 0 or ny >= 2 ** n or ny < 0:
                    continue
                else:
                    if graph[nx][ny] != 0:
                        cnt += 1
            ice[x][y] = cnt

    for x in range(2 ** n):
        for y in range(2 ** n):
            if ice[x][y] < 3:
                if graph[x][y] > 0:
                    graph[x][y] -= 1


def sumIce():
    global answer
    for x in range(2 ** n):
        for y in range(2 ** n):
            answer += graph[x][y]


def bfs(a, b):
    global answer2
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append([a, b])
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 2 ** n or nx < 0 or ny >= 2 ** n or ny < 0 or visited[nx][ny] == 1 or graph[nx][ny] == 0:
                continue
            else:
                queue.append([nx, ny])
                visited[nx][ny] = 1
    answer2 = max(answer2, cnt)


solution()
print(answer)
print(answer2)
