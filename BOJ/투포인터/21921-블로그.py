n, x = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (len(arr) + 1)
answer = 0
cnt = 1
for i in range(1, len(dp)):
    dp[i] = dp[i - 1] + arr[i - 1]
for i in range(n - x + 1):
    end = i + x - 1
    result = dp[end + 1] - dp[i]
    if result > answer:
        answer = result
        cnt = 1
    elif answer == result:
        cnt += 1
if answer == 0:
    print('SAD')
else:
    print(answer)
    print(cnt)
