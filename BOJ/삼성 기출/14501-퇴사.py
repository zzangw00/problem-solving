n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


def solution(n, arr):
    dp = [0 for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        if arr[i][0] + i > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], (arr[i][1] + dp[i + arr[i][0]]))

    return dp


print(max(solution(n, arr)))
