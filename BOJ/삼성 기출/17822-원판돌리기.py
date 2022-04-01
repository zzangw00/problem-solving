from collections import deque
import copy

n, m, t = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(deque(list(map(int, input().split()))))
arr = []
for _ in range(t):
    arr.append(list(map(int, input().split())))
temp = []
for _ in range(n):
    temp.append([0] * m)


def solution():
    answer = 0
    for i in range(t):
        x, d, k = arr[i]
        cycle(x, d, k)
        check()
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                answer += graph[i][j]
    return answer


def cycle(x, d, k):
    global graph
    for i in range(x - 1, n, x):
        if d == 0:
            for _ in range(k):
                a = graph[i].pop()
                graph[i].appendleft(a)
        elif d == 1:
            for _ in range(k):
                a = graph[i].popleft()
                graph[i].append(a)


def check():
    global graph
    visited = copy.deepcopy(temp)
    for i in range(n):
        if graph[i][0] == graph[i][m - 1] and graph[i][0] != 0:
            visited[i][0] = 1
            visited[i][m - 1] = 1
        for j in range(1, m):
            if graph[i][j] == graph[i][j - 1] and graph[i][j] != 0:
                visited[i][j] = 1
                visited[i][j - 1] = 1
    for i in range(m):
        for j in range(1, n):
            if graph[j][i] == graph[j - 1][i] and graph[j][i] != 0:
                visited[j][i] = 1
                visited[j - 1][i] = 1
    cnt = 0
    cnt2 = 0
    num = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                cnt += 1
            if graph[i][j] != 0:
                cnt2 += 1
                num += graph[i][j]
    if cnt == 0:
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 0:
                    if graph[i][j] > num / cnt2:
                        graph[i][j] -= 1
                    elif graph[i][j] < num / cnt2:
                        graph[i][j] += 1
    else:
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 1:
                    graph[i][j] = 0


print(solution())
