n, k = map(int, input().split(' '))
arr = []
for i in range(n):
    arr.append(int(input()))


def solution(n, k, arr):
    answer = 0
    dp = [100000] * (k + 1)
    for i in range(len(dp)):
        for j in range(len(arr)):
            if i == arr[j]:
                dp[i] = 1

    for i in range(1, k + 1):
        for j in arr:
            if j <= i:
                dp[i] = min(dp[i - j] + 1, dp[i])
    if dp[-1] == 100000:
        answer = -1
    else:
        answer = dp[-1]
    return answer


print(solution(n, k, arr))
