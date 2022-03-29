import copy

n, m, k = map(int, input().split())
fire = []
for i in range(m):
    fire.append(list(map(int, input().split())))
graph = []
for _ in range(n):
    graph.append([])
for i in range(n):
    for j in range(n):
        graph[i].append([])
graph2 = []
for _ in range(n):
    graph2.append([])
for i in range(n):
    for j in range(n):
        graph2[i].append([])
for i in range(len(fire)):
    r, c, m, s, d = fire[i]
    graph[r - 1][c - 1].append([m, s, d])
direct = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def solution():
    answer = 0
    for i in range(k):
        move()
        next()
    for i in range(n):
        for j in range(n):
            for p in range(len(graph[i][j])):
                answer += graph[i][j][p][0]
    return answer


def move():
    global graph
    temp = copy.deepcopy(graph2)
    for i in range(n):
        for j in range(n):
            for p in range(len(graph[i][j])):
                m, s, d = graph[i][j][p]
                x = (n + i + (direct[d][0] * s)) % n
                y = (n + j + (direct[d][1] * s)) % n
                temp[x][y].append([m, s, d])
    graph = temp


def next():
    global graph
    temp = copy.deepcopy(graph2)
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) >= 2:
                sumM = 0
                sumS = 0
                check = graph[i][j][0][2] % 2
                flag = 0
                for p in range(len(graph[i][j])):
                    m, s, d = graph[i][j][p]
                    sumM += m
                    sumS += s
                    if d % 2 != check:
                        flag = 1
                if sumM // 5 == 0:
                    graph[i][j] = temp[i][j]
                    continue
                if flag == 0:
                    for p in range(0, 7, 2):
                        m = sumM // 5
                        s = sumS // len(graph[i][j])
                        temp[i][j].append([m, s, p])
                else:
                    for p in range(1, 8, 2):
                        m = sumM // 5
                        s = sumS // len(graph[i][j])
                        temp[i][j].append([m, s, p])
                graph[i][j] = temp[i][j]


print(solution())
