n, m = map(int, input().split())
arr = []
temp = list(map(int, input().split()))
temp.sort()


def dfs(i):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(i, n):
        arr.append(temp[i])
        dfs(i)
        arr.pop()


dfs(0)
