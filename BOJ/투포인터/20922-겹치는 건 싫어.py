n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * (max(arr) + 1)
left = 0
right = 0
answer = 0
while True:
    if cnt[arr[right]] < k:
        cnt[arr[right]] += 1
        right += 1
    else:
        cnt[arr[left]] -= 1
        left += 1
    answer = max(answer, right - left)
    if right >= n:
        break
print(answer)
