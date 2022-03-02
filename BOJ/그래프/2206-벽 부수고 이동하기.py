from collections import deque

n, m = map(int, input().split())
graph = []
answer = 0
for i in range(n):
    graph.append(list(map(int, input())))


def solution(graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = []
    for _ in range(len(graph)):
        visited.append([[0, 0] for _ in range(len(graph[0]))])
    visited[0][0][1] = 1
    queue = deque()
    queue.append((0, 0, 1))

    while queue:
        x, y, k = queue.popleft()
        if x == len(graph) - 1 and y == len(graph[0]) - 1:
            return visited[x][y][k]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(graph) or nx < 0 or ny >= len(graph[0]) or ny < 0:
                continue
            else:
                if graph[nx][ny] == 1 and k == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append((nx, ny, 0))
                elif graph[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx, ny, k))

    return -1


print(solution(graph))
