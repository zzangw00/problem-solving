from collections import deque


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((0, 0))
    graph = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    graph[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(maps) or nx < 0 or ny >= len(maps[0]) or ny < 0:
                continue
            else:
                if maps[nx][ny] == 0 or graph[nx][ny] > -1:
                    continue
                else:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
    return graph[-1][-1]
