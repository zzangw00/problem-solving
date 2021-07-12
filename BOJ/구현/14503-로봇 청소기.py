n, m = map(int, input().split())
r, c, d = map(int, input().split())
dr = [-1, 0, 1, 0]  # 북, 동, 남, 서
dc = [0, 1, 0, -1]
count = 1
graph = []
finish = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]
visited[r][c] = 1
while finish == 0:
    countD = 0
    for i in range(4):
        d = d - 1
        if d < 0:
            d = d + 4
        nr = r + dr[d]
        nc = c + dc[d]
        if graph[nr][nc] == 1 or visited[nr][nc] == 1:
            countD += 1
            if countD == 4:
                nr = r - dr[d]
                nc = c - dc[d]
                if graph[nr][nc] == 1:
                    finish = 1
                else:
                    if visited[nr][nc] == 1:
                        r = nr
                        c = nc
                        break
        else:
            visited[nr][nc] = 1
            r = nr
            c = nc
            count += 1
            break

print(count)
