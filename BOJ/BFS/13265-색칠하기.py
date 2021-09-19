from collections import deque


def bfs(graph, target, visited):
    queue = deque()
    queue.append(target)
    result = 'possible'
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            for j in graph[i]:
                if j in graph[a]:
                    result = 'impossible'
            else:
                if visited[i] == 0:
                    visited[i] = 1
                    queue.append(i)

    return result


t = int(input())
for _ in range(t):
    n, m = map(int, input().split(' '))
    visited = [0] * 1001
    graph = []
    answer = []
    for _ in range(1001):
        graph.append([])
    for _ in range(m):
        x, y = map(int, input().split(' '))
        graph[x].append(y)
        graph[y].append(x)
    for i in range(1, n + 1):
        if visited[i] == 1:
            continue
        else:
            answer.append(bfs(graph, i, visited))
    print(answer)
    if 'impossible' in answer:
        print('impossible')
    else:
        print('possible')
