dust = []
arr = [[0, 0, 2, 0, 0],
       [0, 10, 7, 1, 0],
       [5, 0, 0, 0, 0],
       [0, 10, 7, 1, 0],
       [0, 0, 2, 0, 0]]
dust.append(arr)
for i in range(3):
    arr = list(map(list, reversed([*zip(*arr)])))
    dust.append(arr)
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
answer = 0


def solution():
    d = 0
    stick = []
    stick.append(n // 2)
    stick.append(n // 2)
    flag = 1
    cnt = 0  # 2되면 flag += 1, cnt = 0
    cnt2 = 0  # flag랑 같으면 cnt += 1, cnt2 = 0
    while True:
        x, y = stick
        x += dx[d]
        y += dy[d]
        spread(x, y, d)
        cnt2 += 1
        if cnt2 == flag:
            cnt2 = 0
            cnt += 1
            d = (d + 1) % 4
        if cnt == 2:
            flag += 1
            cnt = 0
        stick = [x, y]
        if x == 0 and y == 0:
            break
    return answer


def spread(x, y, d):
    global graph
    temp = dust[d]
    addedDust = 0
    for i in range(5):
        for j in range(5):
            added = ((graph[x][y] * temp[i][j]) // 100)
            addDust(added, x + i - 2, y + j - 2)
            addedDust += added

    addDust(graph[x][y] - addedDust, x + dx[d], y + dy[d])


def addDust(a, x, y):
    global answer, graph
    if x >= n or x < 0 or y >= n or y < 0:
        answer += a
    else:
        graph[x][y] += a


print(solution())
