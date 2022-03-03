n = int(input())
arr = list(map(int, input().split(' ')))


def solution(n, arr):
    dp = [0] * (n + 1)
    for i in range(1, len(dp)):
        dp[i] = arr[i - 1]
    for i in range(2, n + 1):
        for j in range(len(arr)):
            if i - (j + 1) > 0:
                dp[i] = max(dp[i - (j + 1)] + arr[j], dp[i])

    return dp[-1]


print(solution(n, arr))
