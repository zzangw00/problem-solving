n, m = map(int, input().split())
graph = []
arr1 = []
for i in range(n):
    graph.append(list(map(int, input().split())))
for i in range(m):
    arr1.append(list(map(int, input().split())))
arr = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
visited = []
for i in range(n):
    visited.append([0] * n)
visited[n - 1][0] = 1
visited[n - 1][1] = 1
visited[n - 2][0] = 1
visited[n - 2][1] = 1


def solution():
    for i in range(len(arr1)):
        d, s = arr1[i]
        temp = move(d, s)
        rain(temp)
        cloud(temp)

    answer = check()
    return answer


def move(d, s):
    temp = []
    for x in range(len(graph)):
        for y in range(len(graph)):
            if visited[x][y] == 1:
                nx = (n + x + (arr[d - 1][0] * s)) % n
                ny = (n + y + (arr[d - 1][1] * s)) % n
                temp.append([nx, ny])
                visited[x][y] = 0
    for i in range(len(temp)):
        x, y = temp[i]
        visited[x][y] = 1

    return temp


def rain(temp):
    cross = [[-1, -1], [1, -1], [1, 1], [-1, 1]]
    for i in range(len(temp)):
        x, y = temp[i]
        graph[x][y] += 1
    for i in range(len(temp)):
        x, y = temp[i]
        cnt = 0
        for j in range(4):
            nx = x + cross[j][0]
            ny = y + cross[j][1]
            if nx >= len(graph) or nx < 0 or ny >= len(graph) or ny < 0 or graph[nx][ny] == 0:
                continue
            else:
                cnt += 1
        graph[x][y] += cnt


def cloud(temp):
    for x in range(len(graph)):
        for y in range(len(graph)):
            if graph[x][y] >= 2 and visited[x][y] == 0:
                graph[x][y] -= 2
                visited[x][y] = 1
    for i in range(len(temp)):
        x, y = temp[i]
        visited[x][y] = 0


def check():
    cnt = 0
    for x in range(len(graph)):
        for y in range(len(graph)):
            cnt += graph[x][y]

    return cnt


print(solution())
