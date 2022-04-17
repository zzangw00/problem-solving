n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = []
for _ in range(n):
    visited.append([0] * m)
x = r
y = c
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution():
    global x, y, d, visited
    answer = 0
    cnt = 0
    while True:
        if visited[x][y] == 0:
            visited[x][y] = 1
            answer += 1
        for _ in range(4):
            nx = x + dx[(4 + d - 1) % 4]
            ny = y + dy[(4 + d - 1) % 4]
            if visited[nx][ny] == 1 or graph[nx][ny] == 1:
                d = (4 + d - 1) % 4
                cnt += 1
            else:
                d = (4 + d - 1) % 4
                cnt = 0
                x = nx
                y = ny
                break
        if cnt == 4:
            nx = x + dx[(4 + d - 2) % 4]
            ny = y + dy[(4 + d - 2) % 4]
            if graph[nx][ny] == 1:
                break
            else:
                x = nx
                y = ny
                cnt = 0
    return answer


print(solution())
