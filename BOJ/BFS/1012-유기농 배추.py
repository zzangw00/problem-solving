from collections import deque

t = int(input())
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            else:
                if graph[nx][ny] == 0:
                    continue
                else:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0


for i in range(t):
    m, n, k = map(int, input().split())
    count = 0
    graph = [[0] * m for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                continue
            else:
                bfs(x, y)
                count += 1
    result.append(count)

for i in result:
    print(i)
