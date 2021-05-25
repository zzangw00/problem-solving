from collections import deque

def bfs(arr, x, y):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            else:
                if arr[nx][ny] == 1:
                    continue
                else:
                    queue.append((nx, ny))
                    arr[nx][ny] = 1

n, m = map(int, input().split())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
for i in range(n):
    arr.append(list(map(int, input())))

for x in range(n):
    for y in range(m):
        if arr[x][y] == 1:
            continue
        else:
            bfs(arr, x, y)
            count += 1

print(count)