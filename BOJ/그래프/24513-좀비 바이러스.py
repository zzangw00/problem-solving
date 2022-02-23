from collections import deque

n, m = map(int, input().split())
graph = []
graph2 = []
for _ in range(n):
    graph2.append(list(map(int, input().split())))

for i in range(len(graph2)):
    graph.append([])
    for j in range(len(graph2[i])):
        graph[i].append([graph2[i][j], 0])


def solution(graph):
    answer = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    queue = deque()
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j][0] == 1:
                queue.append((i, j))
            if graph[i][j][0] == 2:
                queue.append((i, j))
    x, y = queue[0]
    bFlag = graph[x][y][0]
    bfs(queue, graph, bFlag)

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j][0] == 1:
                cnt1 += 1
            if graph[i][j][0] == 2:
                cnt2 += 1
            if graph[i][j][0] == 3:
                cnt3 += 1
    answer.append(cnt1)
    answer.append(cnt2)
    answer.append(cnt3)
    return answer


def bfs(queue, graph, bFlag):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    fCnt = 0
    f = bFlag
    while queue:
        x, y = queue.popleft()
        if graph[x][y][0] == 3:
            continue
        flag = graph[x][y][0]
        if flag != bFlag:
            fCnt += 1
            if fCnt == 2:
                cnt += 1
                fCnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(graph) or nx < 0 or ny >= len(graph[0]) or ny < 0:
                continue
            else:
                if graph[x][y][0] == 1 and graph[x][y][0] != f:
                    graph[x][y][1] = cnt
                    if graph[nx][ny][0] == 0:
                        graph[nx][ny][0] = 1
                        graph[nx][ny][1] = cnt
                        queue.append((nx, ny))
                    if graph[nx][ny][0] == 2:
                        if graph[x][y][1] == graph[nx][ny][1]:
                            graph[nx][ny][0] = 3

                if graph[x][y][0] == 1 and graph[x][y][0] == f:
                    if graph[nx][ny][0] == 0:
                        graph[nx][ny][0] = 1
                        graph[nx][ny][1] = cnt
                        queue.append((nx, ny))

                if graph[x][y][0] == 2 and graph[x][y][0] != f:
                    graph[x][y][1] = cnt
                    if graph[nx][ny][0] == 0:
                        graph[nx][ny][0] = 2
                        graph[nx][ny][1] = cnt
                        queue.append((nx, ny))
                    if graph[nx][ny][0] == 1:
                        if graph[x][y][1] == graph[nx][ny][1]:
                            graph[nx][ny][0] = 3

                if graph[x][y][0] == 2 and graph[x][y][0] == f:
                    if graph[nx][ny][0] == 0:
                        graph[nx][ny][0] = 2
                        graph[nx][ny][1] = cnt
                        queue.append((nx, ny))
        bFlag = flag


a = solution(graph)
print(' '.join(map(str, a)))
