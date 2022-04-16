import copy
from collections import deque
from re import L

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            arr.append([i, j])
visited = [0] * len(arr)
temp = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0


def solution():
    dfs(0)
    return answer


def dfs(a):
    if len(temp) == 3:
        check(temp)
        return
    for i in range(a, len(arr)):
        if visited[i] == 0:
            visited[i] = 1
            temp.append(arr[i])
            dfs(i + 1)
            temp.pop()
            visited[i] = 0


def check(temp):
    graph2 = copy.deepcopy(graph)
    for i in range(len(temp)):
        x, y = temp[i]
        graph2[x][y] = 1
    spread(graph2)


def spread(graph2):
    global answer
    cnt = 0
    for x in range(n):
        for y in range(m):
            if graph2[x][y] == 2:
                bfs(graph2, x, y)
    for x in range(n):
        for y in range(m):
            if graph2[x][y] == 0:
                cnt += 1
    answer = max(answer, cnt)


def bfs(graph2, x, y):
    queue = deque([])
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0 or graph2[nx][ny] == 1 or graph2[nx][ny] == 2:
                continue
            else:
                graph2[nx][ny] = 2
                queue.append([nx, ny])


print(solution())
