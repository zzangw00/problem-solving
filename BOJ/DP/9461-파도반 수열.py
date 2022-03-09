dp = [0 for i in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(0, 98):
    dp[i + 3] = dp[i] + dp[i + 1]
t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n])
