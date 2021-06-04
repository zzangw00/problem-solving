n = int(input())
dp = [1] * n
arr = list(map(int, input().split()))
arr.reverse()
for i in range(n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
