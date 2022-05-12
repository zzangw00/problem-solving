from collections import deque


def solution(board):
    dfs(0, 0, len(board), 0, board)
    return min([dfs(0, 0, len(board), 1, board), dfs(0, 0, len(board), 2, board)])


def dfs(r, c, n, d, board):
    visited = []
    for _ in range(n):
        visited.append([0] * n)
    queue = deque()
    queue.append([r, c, d, 0])
    visited[r][c] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        x, y, d, value = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or board[nx][ny] == 1:
                continue
            if i == d:
                nV = value + 100
            else:
                nV = value + 600

            if visited[nx][ny] == 0:
                visited[nx][ny] = nV
                queue.append([nx, ny, i, nV])
            else:
                if nV <= visited[nx][ny]:
                    visited[nx][ny] = nV
                    queue.append([nx, ny, i, nV])
    return visited[-1][-1]
