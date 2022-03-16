n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))
answer = 0


def solution(graph):
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            visited[x][y] = 1
            dfs(x, y, 1, graph[x][y])
            visited[x][y] = 0


def dfs(x, y, cnt, k):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    global answer
    if cnt == 4:
        answer = max(answer, k)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0 or visited[nx][ny] == 1:
            continue
        else:
            visited[nx][ny] = 1
            if cnt == 2:
                dfs(x, y, cnt + 1, k + graph[nx][ny])
            dfs(nx, ny, cnt + 1, k + graph[nx][ny])
            visited[nx][ny] = 0
    return


solution(graph)
print(answer)
