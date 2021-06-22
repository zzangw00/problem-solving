n = int(input())
arr = list(map(int, input().split()))
dp = []
for i in arr:
    dp.append(i)
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(dp)
