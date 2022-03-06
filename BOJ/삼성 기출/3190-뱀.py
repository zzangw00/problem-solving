from collections import deque

n = int(input())
k = int(input())
apple = []
direct = []
direct = deque()
for _ in range(k):
    apple.append(list(map(int, input().split(' '))))
l = int(input())
for _ in range(l):
    a, b = input().split(' ')
    direct.append([int(a), b])
graph = []
for i in range(n):
    graph.append([0] * n)
for i in range(len(apple)):
    graph[apple[i][0] - 1][apple[i][1] - 1] = 2


def solution(graph, direct):
    cnt = 0
    arr = []
    arr = deque()
    arr.append([0, 0])
    graph[0][0] = 1
    dx = [0, -1, 0, 1]  # 동, 북, 서, 남
    dy = [1, 0, -1, 0]
    v = 0
    while True:
        if direct:
            if cnt == direct[0][0]:
                if direct[0][1] == 'L':
                    if v == 3:
                        v = 0
                    else:
                        v += 1
                else:
                    if v == 0:
                        v = 3
                    else:
                        v -= 1
                direct.popleft()
        nx = arr[-1][0] + dx[v]
        ny = arr[-1][1] + dy[v]
        if nx >= len(graph) or nx < 0 or ny >= len(graph) or ny < 0:
            cnt += 1
            break
        elif graph[nx][ny] == 1:
            cnt += 1
            break
        else:
            if graph[nx][ny] == 2:
                arr.append([nx, ny])
                graph[nx][ny] = 1
            else:
                arr.append([nx, ny])
                graph[nx][ny] = 1
                a = arr.popleft()
                graph[a[0]][a[1]] = 0
        cnt += 1

    return cnt


print(solution(graph, direct))
