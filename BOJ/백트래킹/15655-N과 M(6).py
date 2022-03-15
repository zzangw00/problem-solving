n, m = map(int, input().split())
arr = []
temp = list(map(int, input().split()))
visited = [0] * n
temp.sort()


def dfs(a):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(a, n):
        arr.append(temp[i])
        dfs(i + 1)
        arr.pop()


dfs(0)
