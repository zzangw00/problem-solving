n, m = map(int, input().split())
arr = []
temp = list(map(int, input().split()))
temp.sort()


def dfs(a):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(n):
        arr.append(temp[i])
        dfs(a + 1)
        arr.pop()


dfs(0)
