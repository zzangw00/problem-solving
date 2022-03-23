import copy

r, c, t = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))
temp = []
spot = []
for _ in range(r):
    temp.append([0] * c)
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == -1:
            spot.append([i, j])


def solution():
    answer = 0
    for _ in range(t):
        spread()
        upMove()
        downMove()
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if graph[x][y] > 0:
                answer += graph[x][y]
    return answer


def spread():
    arr = copy.deepcopy(temp)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if graph[x][y] != 0 and graph[x][y] != -1:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= len(graph) or nx < 0 or ny >= len(graph[0]) or ny < 0 or graph[nx][ny] == -1:
                        continue
                    else:
                        arr[nx][ny] += (graph[x][y] // 5)
                        cnt += 1
                graph[x][y] -= (cnt * (graph[x][y] // 5))
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            graph[x][y] += arr[x][y]


def upMove():
    before = 0
    d = 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x = spot[0][0]
    y = 1
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if x == spot[0][0] and y == 0:
            break
        if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph[0]):
            d += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny


def downMove():
    before = 0
    d = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = spot[1][0]
    y = 1
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if x == spot[1][0] and y == 0:
            break
        if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph[0]):
            d += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny


print(solution())
