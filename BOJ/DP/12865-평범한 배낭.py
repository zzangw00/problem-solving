n, k = map(int, input().split(' '))
arr = [[0, 0]]
for i in range(n):
    arr.append(list(map(int, input().split(' '))))


def solution(k, arr):
    answer = 0
    dp = []
    for _ in range(len(arr)):
        dp.append([])
    for i in range(len(arr)):
        dp[i] = [0] * (k + 1)

    for i in range(1, len(arr)):
        for j in range(1, k + 1):
            if j < arr[i][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1]
                               [j - arr[i][0]] + arr[i][1])
    return dp[-1][-1]


print(solution(k, arr))
