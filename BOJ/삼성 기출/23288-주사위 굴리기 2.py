from collections import deque
import copy

n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
temp = []
for _ in range(n):
    temp.append([0] * m)
dice = [0, 1, 2, 3, 4, 5, 6]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0


def solution():
    d = 1
    x = 0
    y = 0
    for _ in range(k):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            d = (d + 2) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        x = nx
        y = ny
        roll(x, y)
        diceCheck(d)
        if dice[6] > graph[x][y]:
            d = (d + 1) % 4
        elif dice[6] < graph[x][y]:
            d = (d - 1) % 4
    return answer


def roll(x, y):
    global answer
    a = graph[x][y]
    visited = copy.deepcopy(temp)
    queue = deque([])
    queue.append([x, y])
    visited[x][y] = 1
    answer += a
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0 or visited[nx][ny] == 1:
                continue
            else:
                if graph[nx][ny] == a:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    answer += graph[nx][ny]


def diceCheck(d):
    global dice
    if d == 0:
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
    elif d == 1:
        dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]
    elif d == 2:
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]
    elif d == 3:
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]


print(solution())
