from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
h = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 2:
            h.append([x, y])
visited = [0] * len(h)
temp = []
answer = 1e9
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution():
    k = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 0:
                k += 1
    if k == 0:
        return 0
    dfs(0)
    return answer


def dfs(a):
    if len(temp) == m:
        bfs(temp)
        return
    for i in range(a, len(h)):
        if visited[i] == 0:
            visited[i] = 1
            temp.append(h[i])
            dfs(i + 1)
            temp.pop()
            visited[i] = 0


def bfs(temp):
    global answer
    cnt = 0
    num = 0
    visited = []
    for _ in range(n):
        visited.append([0] * n)
    queue = deque(temp)
    for i in range(len(queue)):
        x, y = queue[i]
        visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or visited[nx][ny] != 0 or graph[nx][ny] == 1:
                continue
            else:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    for x in range(n):
        for y in range(n):
            if graph[x][y] != 2:
                num = max(num, visited[x][y])
            if visited[x][y] == 0 and graph[x][y] == 0:
                cnt += 1
    if cnt == 0:
        answer = min(answer, num - 1)


result = solution()
if result == 1e9:
    print(-1)
else:
    print(result)
