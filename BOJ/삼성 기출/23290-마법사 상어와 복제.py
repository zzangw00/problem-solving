m, t = map(int, input().split())

monster = []
for _ in range(4):
    monster.append([])
for i in range(4):
    for j in range(4):
        monster[i].append([])
pack = []
egg = []
for _ in range(4):
    egg.append([])
for i in range(4):
    for j in range(4):
        egg[i].append([])
death = []
for _ in range(4):
    death.append([])
for i in range(4):
    for j in range(4):
        death[i].append([])
for _ in range(m):
    r, c, d = map(int, input().split())
    monster[r - 1][c - 1].append(d - 1)
r, c = map(int, input().split())
pack.append(r - 1)
pack.append(c - 1)

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx2 = [-1, 0, 1, 0]
dy2 = [0, -1, 0, 1]
temp = []
kk = []


def solution():
    global kk
    answer = 0
    for _ in range(t):
        clone()
        moveM()
        kk = [[9, 9], [9, 9], [9, 9], -1]
        dfs()
        die()
        born()
    for x in range(4):
        for y in range(4):
            answer += len(monster[x][y])
    return answer


def clone():
    global egg
    for x in range(4):
        for y in range(4):
            for p in range(len(monster[x][y])):
                egg[x][y].append(monster[x][y][p])


def moveM():
    global monster
    temp = []
    for _ in range(4):
        temp.append([])
    for i in range(4):
        for j in range(4):
            temp[i].append([])
    for x in range(4):
        for y in range(4):
            for p in range(len(monster[x][y])):
                d = monster[x][y].pop()
                cnt = 0
                for _ in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx >= 4 or nx < 0 or ny >= 4 or ny < 0 or len(death[nx][ny]) > 0 or (nx == pack[0] and ny == pack[1]):
                        d = (d - 1 + 8) % 8
                        cnt += 1
                    else:
                        temp[nx][ny].append(d)
                        break
                if cnt == 8:
                    temp[x][y].append(d)
    monster = temp


def dfs():
    if len(temp) == 3:
        moveP(temp)
        return
    for i in range(4):
        temp.append(i)
        dfs()
        temp.pop()


def moveP(temp):
    global kk, pack
    visited = []
    for _ in range(4):
        visited.append([0] * 4)
    x = pack[0]
    y = pack[1]
    eat = 0
    arr = []
    for i in temp:
        nx = x + dx2[i]
        ny = y + dy2[i]
        if nx >= 4 or nx < 0 or ny >= 4 or ny < 0:
            return
        else:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                eat += len(monster[nx][ny])
            arr.append([nx, ny])
            x = nx
            y = ny
    if kk[3] < eat:
        kk[0] = arr[0]
        kk[1] = arr[1]
        kk[2] = arr[2]
        kk[3] = eat


def die():
    global monster, death, pack
    pack = kk[2]
    for x in range(4):
        for y in range(4):
            temp = []
            for p in range(len(death[x][y])):
                a = death[x][y].pop()
                a -= 1
                if a > 0:
                    temp.append(a)
            death[x][y] = temp
    for i in range(len(kk) - 1):
        x, y = kk[i]
        for j in range(len(monster[x][y])):
            death[x][y].append(2)
        monster[x][y] = []


def born():
    global egg, monster
    for x in range(4):
        for y in range(4):
            for p in range(len(egg[x][y])):
                a = egg[x][y].pop()
                monster[x][y].append(a)


print(solution())
