from collections import deque
n, m, k = map(int, input().split())
yb = []
for i in range(n):
    yb.append([5] * n)
add = []
for i in range(n):
    add.append(list(map(int, input().split())))
namu = []
for i in range(n):
    namu.append([])
for i in range(n):
    for j in range(n):
        namu[i].append(deque([]))
for i in range(m):
    x, y, z = map(int, input().split())
    namu[x - 1][y - 1].append(z)
round = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def spring():
    for x in range(n):
        for y in range(n):
            for p in range(len(namu[x][y])):
                if yb[x][y] >= namu[x][y][p]:
                    yb[x][y] -= namu[x][y][p]
                    namu[x][y][p] += 1
                else:
                    for _ in range(p, len(namu[x][y])):
                        yb[x][y] += (namu[x][y].pop() // 2)
                    break


def fall():
    for x in range(n):
        for y in range(n):
            for p in range(len(namu[x][y])):
                a = namu[x][y][p]
                if a % 5 == 0:
                    for j in range(8):
                        nx = x + round[j][0]
                        ny = y + round[j][1]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        else:
                            namu[nx][ny].appendleft(1)
            yb[x][y] += add[x][y]


answer = 0
for _ in range(k):
    spring()
    fall()
for x in range(n):
    for y in range(n):
        answer += len(namu[x][y])

print(answer)
