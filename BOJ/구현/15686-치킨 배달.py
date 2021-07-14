import itertools

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

chickenList = []
houseList = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickenList.append((i, j))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houseList.append((i, j))

result = 100000000
for i in range(1, m + 1):
    combination = list(itertools.combinations(chickenList, i))
    for c in combination:
        dist = 0
        for h in houseList:
            minDist = min([abs(p[0] - h[0]) + abs(p[1] - h[1]) for p in c])
            dist += minDist
        if dist < result:
            result = dist

print(result)
