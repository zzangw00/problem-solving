import copy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
temp = []
move = [[],
        [[0], [1], [2], [3]],
        [[1, 3], [0, 2]],
        [[1, 0], [0, 3], [3, 2], [1, 2]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 1e9


def solution():
    arr = []
    for i in range(n):
        for j in range(m):
            if 1 <= graph[i][j] <= 5:
                arr.append([i, j, graph[i][j]])
    dfs(arr, 0)
    return answer


def dfs(arr, a):
    if len(temp) == len(arr):
        check(temp, arr)
        return
    for i in range(a, len(arr)):
        for j in range(len(move[arr[i][2]])):
            temp.append(move[arr[i][2]][j])
            dfs(arr, i + 1)
            temp.pop()


def check(temp, arr):
    global answer
    cnt = 0
    visited = copy.deepcopy(graph)
    for i in range(len(arr)):
        a, b, v = arr[i]
        for d in temp[i]:
            x = a
            y = b
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                if nx >= n or nx < 0 or ny >= m or ny < 0 or graph[nx][ny] == 6:
                    break
                else:
                    visited[nx][ny] = 1
                    x = nx
                    y = ny
    for x in range(n):
        for y in range(m):
            if visited[x][y] == 0:
                cnt += 1
    answer = min(answer, cnt)


print(solution())
