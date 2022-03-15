from logging import makeLogRecord


n, m = map(int, input().split())

arr = []


def dfs(i):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(i, n + 1):
        arr.append(i)
        dfs(i)
        arr.pop()


dfs(1)
