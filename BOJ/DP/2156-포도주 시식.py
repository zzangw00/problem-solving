import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
dp = [0] * 10000
dp[0] = arr[0]
if n > 1:
    dp[1] = dp[0] + arr[1]
if n > 2:
    dp[2] = max(dp[1], dp[0] + arr[2], arr[1] + arr[2])
    for i in range(3, n):
        dp[i] = max(dp[i - 1], dp[i - 3] + arr[i - 1] +
                    arr[i], dp[i - 2] + arr[i])

print(max(dp))
