n, m = map(int, input().split())
arr = []
temp = list(map(int, input().split()))
temp.sort()
visited = [0] * n


def dfs(i):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(len(temp)):
        if visited[i] == 0:
            arr.append(temp[i])
            visited[i] = 1
            dfs(i + 1)
            arr.pop()
            visited[i] = 0


dfs(0)
