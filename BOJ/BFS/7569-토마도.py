from collections import deque

m, n, h = map(int, input().split())
graph = []

for i in range(h):
    graph.append([])
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))


def solution(graph):
    cnt = 0
    answer = 0
    queue = deque()
    visited = []
    for i in range(h):
        visited.append([])
    for i in range(h):
        for j in range(n):
            visited[i].append([-1 for _ in range(m)])
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 1:
                    visited[z][x][y] = 0
                    queue.append((z, x, y))

    answer = bfs(z, x, y, queue, visited) - 1

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 0:
                    cnt += 1
    if cnt == 0:
        answer = answer
    else:
        answer = -1

    return answer


def bfs(z, x, y, queue, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dz = [-1, 1]
    day = 0
    pCnt = len(queue)
    qCnt = 0
    while queue:
        z, x, y = queue.popleft()
        pCnt -= 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(graph[0]) or nx < 0 or ny >= len(graph[0][0]) or ny < 0:
                continue
            else:
                if graph[z][nx][ny] == 0:
                    queue.append((z, nx, ny))
                    qCnt += 1
                    graph[z][nx][ny] = 1
                    visited[z][nx][ny] = day
                else:
                    continue
        for i in range(2):
            nz = z + dz[i]
            if nz >= len(graph) or nz < 0:
                continue
            else:
                if graph[nz][x][y] == 0:
                    queue.append((nz, x, y))
                    qCnt += 1
                    graph[nz][x][y] = 1
                    visited[nz][x][y] = day
                else:
                    continue
        if pCnt == 0:
            day += 1
            pCnt = qCnt
            qCnt = 0
    return day


print(solution(graph))
