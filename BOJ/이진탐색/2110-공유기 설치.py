n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0
while (start <= end):
    mid = (start + end) // 2
    current = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            current = arr[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
