n, m = map(int, input().split())

arr = []
visited = [0] * (n + 1)


def dfs(a):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(a, n + 1):
        if visited[i] == 0:
            arr.append(i)
            visited[i] = 1
            dfs(i + 1)
            arr.pop()
            visited[i] = 0


dfs(1)
