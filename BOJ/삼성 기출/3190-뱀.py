from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append([0] * n)
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
l = int(input())
direct = []
for _ in range(l):
    direct.append(list(input().split()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution():
    answer = 0
    d = 1
    snake = deque([[0, 0]])
    visited = []
    for _ in range(n):
        visited.append([0] * n)
    visited[0][0] = 1
    while True:
        answer += 1
        x = snake[0][0]
        y = snake[0][1]
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= n or nx < 0 or ny >= n or ny < 0 or visited[nx][ny] == 1:
            break
        else:
            if graph[nx][ny] == 1:
                visited[nx][ny] = 1
                snake.appendleft([nx, ny])
                graph[nx][ny] = 0
            else:
                visited[nx][ny] = 1
                snake.appendleft([nx, ny])
                a, b = snake.pop()
                visited[a][b] = 0
        for i in range(len(direct)):
            if answer == int(direct[i][0]):
                if direct[i][1] == 'L':
                    d = ((d - 1) + 4) % 4
                else:
                    d = ((d + 1) + 4) % 4
    return answer


print(solution())
