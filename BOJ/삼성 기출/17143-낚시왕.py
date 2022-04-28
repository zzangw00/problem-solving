r, c, m = map(int, input().split())
graph = []
for _ in range(r):
    graph.append([])
for i in range(r):
    for j in range(c):
        graph[i].append([])

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    graph[x - 1][y - 1].append([s, d - 1, z])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0


def solution():
    for y in range(c):
        catch(y)
        move()
    return answer


def catch(y):
    global graph, answer
    for x in range(r):
        if graph[x][y]:
            for p in range(len(graph[x][y])):
                s, d, z = graph[x][y].pop()
                answer += z
            break


def move():
    global graph
    temp = []
    for _ in range(r):
        temp.append([])
    for i in range(r):
        for j in range(c):
            temp[i].append([])
    for x in range(r):
        for y in range(c):
            for p in range(len(graph[x][y])):
                s, d, z = graph[x][y].pop()
                a = x
                b = y
                for i in range(s):
                    nx = a + dx[d]
                    ny = b + dy[d]
                    if nx >= r or nx < 0 or ny >= c or ny < 0:
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2
                        nx = a + dx[d]
                        ny = b + dy[d]
                    a = nx
                    b = ny
                if temp[a][b]:
                    if temp[a][b][0][2] < z:
                        temp[a][b].pop()
                        temp[a][b].append([s, d, z])
                else:
                    temp[a][b].append([s, d, z])
    graph = temp


print(solution())
