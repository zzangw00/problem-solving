from collections import deque


def bfs(graph, target, visited):
    queue = deque()
    queue.append(target)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)


def solution(n, computers):
    answer = 0
    visited = [0] * (n + 1)
    graph = []
    for i in range(n + 1):
        graph.append([])
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                graph[i + 1].append(j + 1)
    for i in range(1, n + 1):
        for j in graph[i]:
            if i == j:
                graph[i].remove(j)
    for i in range(1, n + 1):
        if visited[i] == 1:
            continue
        else:
            bfs(graph, i, visited)
            answer += 1

    return answer
