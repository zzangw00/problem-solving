from collections import deque
import copy

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
temp = []
for _ in range(n):
    temp.append([0] * n)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
baby = []
size = 2
cnt = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == 9:
            baby.append(x)
            baby.append(y)


def solution():
    answer = 0
    while True:
        flag, d = bfs(baby)
        answer += d
        if flag == 1:
            break
    return answer


def bfs(spot):
    global cnt
    global size
    global baby
    global graph
    visited = copy.deepcopy(temp)
    minValue = []
    queue = deque()
    x, y = spot
    visited[x][y] = 1
    graph[x][y] = 0
    queue.append([x, y])
    lenQ = 1
    cntQ = 0
    distance = 1
    d = 1e9
    while queue:
        x, y = queue.popleft()
        lenQ -= 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or graph[nx][ny] > size or visited[nx][ny] != 0:
                continue
            else:
                if graph[nx][ny] == size or graph[nx][ny] == 0:
                    queue.append([nx, ny])
                    cntQ += 1
                    visited[nx][ny] = distance
                elif graph[nx][ny] < size:
                    queue.append([nx, ny])
                    cntQ += 1
                    visited[nx][ny] = distance
                    if d > distance:
                        d = distance
                        minValue = [nx, ny]
                    elif d == distance:
                        q, w = minValue
                        if nx < q:
                            minValue = [nx, ny]
                        elif nx == q:
                            if ny < w:
                                minValue = [nx, ny]
        if lenQ == 0:
            distance += 1
            lenQ += cntQ
            cntQ = 0

    if not minValue:
        return 1, 0
    else:
        cnt += 1
        baby = minValue
        if cnt == size:
            size += 1
            cnt = 0
        k, m = minValue
        distance = visited[k][m]
        return 0, distance


print(solution())
