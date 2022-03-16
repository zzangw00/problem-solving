n, m = map(int, input().split())
arr = []
temp = list(map(int, input().split()))
temp.sort()
answer = []


def dfs(a):
    if len(arr) == m:
        answer.append(list(arr))
        return
    for i in range(n):
        arr.append(temp[i])
        dfs(a + 1)
        arr.pop()


dfs(0)

result = list(set(map(tuple, answer)))
result.sort()
for i in result:
    print(*i)
