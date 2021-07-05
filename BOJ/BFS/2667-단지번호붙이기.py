from collections import deque
n = int(input())
graph = []
cnt = 0
result = []
dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    cnt2 = 0
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        cnt2 += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            else:
                if graph[nx][ny] == 0:
                    continue
                else:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0
    result.append(cnt2)


for x in range(n):
    for y in range(n):
        if graph[x][y] == 0:
            continue
        else:
            bfs(x, y)
            cnt += 1

print(cnt)
result.sort()
for i in range(len(result)):
    print(result[i])
