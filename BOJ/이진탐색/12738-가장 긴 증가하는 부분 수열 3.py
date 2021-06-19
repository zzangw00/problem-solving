from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp = []
for i in arr:
    temp = bisect_left(dp, i)
    if len(dp) <= temp:
        dp.append(i)
    else:
        dp[temp] = i
print(len(dp))
