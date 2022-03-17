n = int(input())
graph = list(map(int, input().split()))
m = list(map(int, input().split()))
k = []
maxValue = -1000000000
minValue = 1000000000
for i in range(len(m)):
    for j in range(m[i]):
        k.append(i + 1)
visited = [0] * len(k)
arr = []


def solution():
    dfs(0)


def dfs(a):
    global maxValue
    global minValue
    if len(arr) == len(graph) - 1:
        temp = graph[0]
        for i in range(len(arr)):
            if arr[i] == 1:
                temp += graph[i + 1]
            elif arr[i] == 2:
                temp -= graph[i + 1]
            elif arr[i] == 3:
                temp = temp * graph[i + 1]
            elif arr[i] == 4:
                if temp < 0 and graph[i + 1] > 0:
                    temp = -temp
                    temp = temp // graph[i + 1]
                    temp = -temp
                else:
                    temp = temp // graph[i + 1]
        maxValue = max(maxValue, temp)
        minValue = min(minValue, temp)
        return
    for i in range(len(k)):
        if visited[i] == 0:
            arr.append(k[i])
            visited[i] = 1
            dfs(a + 1)
            arr.pop()
            visited[i] = 0


solution()
print(maxValue)
print(minValue)
