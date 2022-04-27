from collections import deque, defaultdict

n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
wall = defaultdict(set)
w = int(input())
for _ in range(w):
    x, y, s = map(int, input().split())
    if s == 0:
        wall[(x - 1, y - 1)].add((x - 2, y - 1))
        wall[(x - 2, y - 1)].add((x - 1, y - 1))
    else:
        wall[(x - 1, y - 1)].add((x - 1, y))
        wall[(x - 1, y)].add((x - 1, y - 1))
arr = []
flag = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 or graph[i][j] == 2 or graph[i][j] == 3 or graph[i][j] == 4:
            arr.append([i, j, graph[i][j]])
for x in range(n):
    for y in range(m):
        if graph[x][y] == 5:
            flag += 1
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
move = [[],
        [1, 2, 3],
        [5, 6, 7],
        [7, 0, 1],
        [3, 4, 5]]
answer = 0


def solution():
    temp2 = []
    for _ in range(n):
        temp2.append([0] * m)
    for _ in range(100):
        graph2 = spread(temp2)
        graph3 = shake(graph2)
        temp2 = graph3
        cnt = 0
        for x in range(n):
            for y in range(m):
                if temp2[x][y] >= k and graph[x][y] == 5:
                    cnt += 1
        if cnt == flag:
            return answer
    return 101


def spread(temp2):
    for i in range(len(arr)):
        visited = []
        for _ in range(n):
            visited.append([0] * m)
        visited2 = []
        for _ in range(n):
            visited2.append([0] * m)
        queue = deque([])
        x, y, a = arr[i]
        nx = x + dx[move[a][1]]
        ny = y + dy[move[a][1]]
        visited[x + dx[move[a][1]]][y + dy[move[a][1]]] = 5
        visited2[x + dx[move[a][1]]][y + dy[move[a][1]]] = 1
        temp2[x + dx[move[a][1]]][y + dy[move[a][1]]] += 5
        queue.append([nx, ny, a])
        while queue:
            x, y, a = queue.popleft()
            if visited[x][y] == 0:
                break
            for i in range(3):
                nx = x + dx[move[a][i]]
                ny = y + dy[move[a][i]]
                if nx >= n or nx < 0 or ny >= m or ny < 0:
                    continue
                if a == 2:
                    if i == 1 and (x, y) in wall[(nx, ny)]:
                        continue
                    if (i == 0 and (x + 1, y) in wall[(x, y)]) or (i == 0 and (x + 1, y) in wall[(nx, ny)]):
                        continue
                    if (i == 2 and (x - 1, y) in wall[(x, y)]) or (i == 2 and (x - 1, y) in wall[(nx, ny)]):
                        continue
                if a == 3:
                    if i == 1 and (x, y) in wall[(nx, ny)]:
                        continue
                    if (i == 0 and (x, y) in wall[(x, y - 1)]) or (i == 0 and (x, y - 1) in wall[(nx, ny)]):
                        continue
                    if (i == 2 and (x, y) in wall[(x, y + 1)]) or (i == 2 and (x, y + 1) in wall[(nx, ny)]):
                        continue
                if a == 1:
                    if i == 1 and (x, y) in wall[(nx, ny)]:
                        continue
                    if (i == 0 and (x - 1, y) in wall[(x, y)]) or (i == 0 and (x - 1, y) in wall[(nx, ny)]):
                        continue
                    if (i == 2 and (x + 1, y) in wall[(x, y)]) or (i == 2 and (x + 1, y) in wall[(nx, ny)]):
                        continue
                if a == 4:
                    if i == 1 and (x, y) in wall[(nx, ny)]:
                        continue
                    if (i == 0 and (x, y) in wall[(x, y + 1)]) or (i == 0 and (x, y + 1) in wall[(nx, ny)]):
                        continue
                    if (i == 2 and (x, y) in wall[(x, y - 1)]) or (i == 2 and (x, y - 1) in wall[(nx, ny)]):
                        continue
                if visited2[nx][ny] == 0:
                    temp2[nx][ny] += visited[x][y] - 1
                visited[nx][ny] = visited[x][y] - 1
                visited2[nx][ny] = 1
                queue.append([nx, ny, a])
    return temp2


def shake(graph):
    global answer
    answer += 1
    visited = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for _ in range(n):
        visited.append([0] * m)
    for x in range(n):
        for y in range(m):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= n or nx < 0 or ny >= m or ny < 0 or (x, y) in wall[nx, ny]:
                    continue
                else:
                    if graph[x][y] - graph[nx][ny] >= 4:
                        visited[nx][ny] += ((graph[x][y] - graph[nx][ny]) // 4)
                        visited[x][y] -= ((graph[x][y] - graph[nx][ny]) // 4)
    for x in range(n):
        for y in range(m):
            graph[x][y] += visited[x][y]

    for i in range(m - 1):
        if graph[0][i] > 0:
            graph[0][i] -= 1
    for i in range(n - 1):
        if graph[i][m - 1] > 0:
            graph[i][m - 1] -= 1
    for i in range(m - 1, 0, -1):
        if graph[n - 1][i] > 0:
            graph[n - 1][i] -= 1
    for i in range(n - 1, 0, -1):
        if graph[i][0] > 0:
            graph[i][0] -= 1
    return graph


print(solution())
