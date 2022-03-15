n, m = map(int, input().split())
arr = []
temp = list(map(int, input().split()))
temp.sort()
answer = []
visited = [0] * n


def dfs():
    if len(arr) == m:
        answer.append(list(arr))
        return
    for i in range(n):
        if visited[i] == 0:
            arr.append(temp[i])
            visited[i] = 1
            dfs()
            arr.pop()
            visited[i] = 0


dfs()

result = list(set(map(tuple, answer)))
result.sort()
for i in result:
    print(*i)
