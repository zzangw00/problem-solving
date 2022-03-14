n, m = map(int, input().split())

arr = []


def dfs(a):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(a, n + 1):
        arr.append(i)
        dfs(i)
        arr.pop()


dfs(1)
