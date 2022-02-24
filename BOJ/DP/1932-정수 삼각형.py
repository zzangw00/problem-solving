n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split(' '))))


def solution(graph):
    answer = 0
    dp = []
    for i in range(0, len(graph)):
        dp.append([0 for _ in range(i + 1)])

    dp[0][0] = graph[0][0]
    for i in range(1, len(graph)):
        for j in range(len(graph[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + graph[i][j]
            elif j == len(graph[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + graph[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + graph[i][j],
                               dp[i - 1][j] + graph[i][j])

    answer = max(dp[len(dp) - 1])
    return answer


print(solution(graph))
