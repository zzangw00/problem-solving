from collections import deque

n = int(input())
m = int(input())
graph = []
for i in range(n + 1):
    graph.append([])

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
visited[1] = 1


def bfs(graph):
    queue = deque()
    queue.append(1)
    count = 0
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                count += 1
    return count


print(bfs(graph))
