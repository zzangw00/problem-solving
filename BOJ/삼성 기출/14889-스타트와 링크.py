n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [0] * n
answer = 1e9


def dfs(a, cnt):
    global answer
    if cnt == n // 2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] == 1 and visited[j] == 1:
                    start += graph[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    link += graph[i][j]
        answer = min(answer, abs(start - link))
    for i in range(a, n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i + 1, cnt + 1)
            visited[i] = 0


dfs(0, 0)
print(answer)
