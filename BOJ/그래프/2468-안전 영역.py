from collections import deque
import copy

n = int(input())
arr = []
maxArr = []

for i in range(n):
    arr.append(list(map(int, input().split(' '))))
for i in range(n):
    maxArr.append(max(arr[i]))
maxValue = max(maxArr)


def solution(n, arr, maxValue):
    answer = []
    for k in range(maxValue + 1):
        cnt = 0
        map = copy.deepcopy(arr)
        for x in range(n):
            for y in range(n):
                if map[x][y] <= k:
                    map[x][y] = 0
        for x in range(n):
            for y in range(n):
                if map[x][y] == 0:
                    continue
                else:
                    bfs(map, x, y)
                    cnt += 1
        answer.append(cnt)
    return max(answer)


def bfs(map, x, y):
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    map[x][y] = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(map) or nx < 0 or ny >= len(map[0]) or ny < 0:
                continue
            else:
                if map[nx][ny] == 0:
                    continue
                else:
                    queue.append((nx, ny))
                    map[nx][ny] = 0


print(solution(n, arr, maxValue))
