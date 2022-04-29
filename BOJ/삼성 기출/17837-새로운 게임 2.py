import copy

n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
chess = []
for _ in range(n):
    chess.append([])
for i in range(n):
    for j in range(n):
        chess[i].append([])
spot = [[]]
for i in range(k):
    x, y, d = map(int, input().split())
    spot.append([x - 1, y - 1])
    chess[x - 1][y - 1].append([i + 1, d - 1])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def solution():
    for i in range(1000):
        flag = move()
        if flag == 1:
            return i + 1
    return -1


def move():
    global chess, spot
    flag = 0
    for i in range(1, len(spot)):
        r, c = spot[i]
        arr = copy.deepcopy(chess[r][c])
        temp = []
        a = 0
        for j in range(len(arr)):
            if arr[j][0] == i:
                a = j
        for p in range(a, len(arr)):
            temp.append(arr[p])
        for p in range(len(temp)):
            chess[r][c].pop()
        x = r
        y = c
        q, d = arr[a]
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= n or nx < 0 or ny >= n or ny < 0 or graph[nx][ny] == 2:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= n or nx < 0 or ny >= n or ny < 0 or graph[nx][ny] == 2:
                d = d
                for w in range(len(temp)):
                    if temp[w][0] == i:
                        chess[x][y].append([temp[w][0], d])
                    else:
                        chess[x][y].append([temp[w][0], temp[w][1]])
                    spot[temp[w][0]] = [x, y]
            else:
                if graph[nx][ny] == 0:
                    for w in range(len(temp)):
                        if temp[w][0] == i:
                            chess[nx][ny].append([temp[w][0], d])
                        else:
                            chess[nx][ny].append([temp[w][0], temp[w][1]])
                        spot[temp[w][0]] = [nx, ny]
                elif graph[nx][ny] == 1:
                    for w in range(len(temp)):
                        kk, qq = temp.pop()
                        if kk == i:
                            chess[nx][ny].append([kk, d])
                        else:
                            chess[nx][ny].append([kk, qq])
                        spot[kk] = [nx, ny]
                if len(chess[nx][ny]) >= 4:
                    flag = 1
        else:
            if graph[nx][ny] == 0:
                for w in range(len(temp)):
                    chess[nx][ny].append(temp[w])
                    spot[temp[w][0]] = [nx, ny]
            elif graph[nx][ny] == 1:
                for w in range(len(temp)):
                    kk, qq = temp.pop()
                    chess[nx][ny].append([kk, qq])
                    spot[kk] = [nx, ny]
            if len(chess[nx][ny]) >= 4:
                flag = 1

    return flag


print(solution())
