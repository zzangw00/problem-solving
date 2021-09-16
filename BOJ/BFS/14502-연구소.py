from collections import deque
from itertools import combinations
import copy
n, m = map(int, input().split())
graph = []
answer = []
empty = []
dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]
for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y, a):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            else:
                if a[nx][ny] == 0:
                    a[nx][ny] = 2
                    queue.append((nx, ny))
                else:
                    continue


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))
com = list(combinations(empty, 3))

for i in range(len(com)):
    a = copy.deepcopy(graph)
    cnt = 0
    for j in range(len(com[i])):
        x = com[i][j][0]
        y = com[i][j][1]
        a[x][y] = 1
    for k in range(n):
        for z in range(m):
            if a[k][z] == 2:
                bfs(k, z, a)
    for q in range(n):
        for t in range(m):
            if a[q][t] == 0:
                cnt += 1
    answer.append(cnt)
print(max(answer))
