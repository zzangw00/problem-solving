n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

start = arr[1] - arr[0]
end = arr[n - 1] - arr[0]
result = []
while start <= end:
    mid = (start + end) // 2
    current = arr[0]
    cnt = 1
    for i in range(1, n):
        if current + mid <= arr[i]:
            current = arr[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result.append(mid)
    else:
        end = mid - 1
print(max(result))
