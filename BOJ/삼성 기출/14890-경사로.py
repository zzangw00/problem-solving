import copy

n, l = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
answer = 0
arr = []
for _ in range(n):
    arr.append([0] * n)


def solution():
    global graph

    check()
    temp = []
    for i in zip(*graph):
        temp.append(list(i))
    graph = temp
    check()

    return answer


def check():
    global answer
    visited = copy.deepcopy(arr)
    for x in range(n):
        flag = 0
        for y in range(1, n):
            if graph[x][y] == graph[x][y - 1]:
                continue
            else:
                if abs(graph[x][y] - graph[x][y - 1]) >= 2:
                    flag = 1
                    break
                if graph[x][y] > graph[x][y - 1]:
                    if y - l >= 0 and visited[x][y - l:y] == [0] * l and graph[x][y - l:y] == [graph[x][y - 1]] * l:
                        visited[x][y - l:y] = [1] * l
                        continue
                    else:
                        flag = 1
                        break
                elif graph[x][y] < graph[x][y - 1]:
                    if y - 1 + l < n and visited[x][y:y + l] == [0] * l and graph[x][y:y + l] == [graph[x][y]] * l:
                        visited[x][y:y + 1] = [1] * l
                        continue
                    else:
                        flag = 1
                        break
        if flag == 0:
            answer += 1


print(solution())
