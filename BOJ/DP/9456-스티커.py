t = int(input())


def solution(t):
    for _ in range(t):
        dp = []
        n = int(input())
        arr = []
        answer = []
        for _ in range(2):
            arr.append(list(map(int, input().split())))
            dp.append([0 for _ in range(len(arr[0]) + 1)])
        dp[0][0] = 0
        dp[1][0] = 0
        dp[0][1] = arr[0][0]
        dp[1][1] = arr[1][0]
        for i in range(2, len(arr[0]) + 1):
            dp[0][i] = max((dp[1][i - 1] + arr[0][i - 1]),
                           (dp[1][i - 2] + arr[0][i - 1]))
            dp[1][i] = max((dp[0][i - 1] + arr[1][i - 1]),
                           (dp[0][i - 2] + arr[1][i - 1]))
        for i in range(2):
            answer.append(max(dp[i]))
        print(max(answer))


solution(t)
