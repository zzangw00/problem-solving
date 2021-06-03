t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    graph = list(map(int, input().split()))
    dp = []
    start = 0
    for i in range(n):
        dp.append(graph[start: start + m])
        start += m

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                leftUp = 0
            else:
                leftUp = dp[j - 1][i - 1]
            if j == n - 1:
                leftDown = 0
            else:
                leftDown = dp[j + 1][i - 1]
            left = dp[j][i - 1]
            dp[j][i] = dp[j][i] + max(leftUp, leftDown, left)

    result = []
    for i in range(n):
        result.append(dp[i][m - 1])

    print(max(result))
