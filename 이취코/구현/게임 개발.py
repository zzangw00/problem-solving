n, m = map(int, input().split())
x, y, direct = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visitedMap = []
for i in range(n):
    visitedMap.append([0] * m)

visitedMap[x][y] = 1
dx = [-1, 0, 1, 0] #북, 서, 남,
dy = [0, -1, 0, 1]

count = 1
turnTime = 0

while True:
    direct = direct - 1
    if direct == -1:
        direct = 3
    nx = x + dx[direct]
    ny = y + dy[direct]
    if visitedMap[nx][ny] == 0 and arr[nx][ny] == 0:
        visitedMap[nx][ny] = 1
        x = nx
        y = ny
        count = count + 1
        turnTime = 0
    else:
        turnTime = turnTime + 1
    if turnTime == 4:
        nx = x - dx[direct]
        ny = y - dy[direct]
        if visitedMap[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break

print(count)