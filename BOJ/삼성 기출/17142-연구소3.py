from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
b = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 2:
            b.append([x, y])
virus = list(combinations(b, m))
temp = []
aCnt = 0
for _ in range(n):
    temp.append([0] * n)
for x in range(n):
    for y in range(n):
        if graph[x][y] == 2:
            temp[x][y] = '*'
        elif graph[x][y] == 1:
            temp[x][y] = '-'
        else:
            aCnt += 1
            temp[x][y] = 0


def solution():
    answer = 1e9
    for i in range(len(virus)):
        arr = copy.deepcopy(temp)
        for j in range(len(virus[i])):
            x, y = virus[i][j]
            arr[x][y] = -1
        a = bfs(arr, virus[i])
        answer = min(answer, a)
    if answer == 1e9:
        answer = -1
    return answer


def bfs(arr, virus):
    visited = []
    result = 0
    for _ in range(n):
        visited.append([0] * n)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque(virus)
    time = 1
    cnt = len(queue)
    pushCnt = 0
    p = 0
    aaa = 0
    ax = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 0:
                p += 1
    if p == 0:
        return 0
    while queue:
        x, y = queue.popleft()
        cnt -= 1
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or visited[nx][ny] == 1 or arr[nx][ny] == '-' or arr[nx][ny] == -1:
                continue
            else:
                if arr[nx][ny] == 0:
                    aaa += 1
                arr[nx][ny] = time
                pushCnt += 1
                queue.append([nx, ny])
                visited[nx][ny] = 1
                if aaa == aCnt:
                    ax += 1
                    break
        if ax == 1:
            break
        if cnt == 0:
            time += 1
            cnt = pushCnt
            pushCnt = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 0:
                return 1e9
            z = str(arr[x][y])
            if z.isdigit() == True:
                result = max(result, arr[x][y])
    return result


print(solution())
