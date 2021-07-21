from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
count = 0
for i in range(n + 1):
    arr.append([])
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (n + 1)


def bfs(arr, target):
    queue = deque()
    queue.append(target)
    while queue:
        a = queue.popleft()
        for i in arr[a]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)


for i in range(1, n + 1):
    if visited[i] == 1:
        continue
    else:
        bfs(arr, i)
        count += 1

print(count)
