import copy
from collections import deque
n, l, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def solution(arr, l, r):
    answer = 0
    graph = []
    for _ in range(len(arr)):
        graph.append([0] * len(arr))
    while True:
        cnt = 1
        visited = copy.deepcopy(graph)
        num = []
        for x in range(len(arr)):
            for y in range(len(arr)):
                if visited[x][y] == 0:
                    a = bfs(x, y, cnt, arr, visited, l, r)
                    if a > 0:
                        cnt += 1
        if cnt == 1:
            break
        else:
            for i in range(1, cnt):
                result = 0
                cnt2 = 0
                for x in range(len(arr)):
                    for y in range(len(arr)):
                        if visited[x][y] == i:
                            cnt2 += 1
                            result += arr[x][y]
                num.append(int(result // cnt2))
            for i in range(cnt - 1):
                for x in range(len(arr)):
                    for y in range(len(arr)):
                        if visited[x][y] == i + 1:
                            arr[x][y] = num[i]
        answer += 1

    return answer


def bfs(x, y, cnt, arr, visited, l, r):
    flag = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([])
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(arr) or nx < 0 or ny >= len(arr) or ny < 0:
                continue
            else:
                if visited[nx][ny] == 0:
                    if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                        visited[x][y] = cnt
                        visited[nx][ny] = cnt
                        queue.append((nx, ny))
                        flag += 1
    return flag


print(solution(arr, l, r))
