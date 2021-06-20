n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
start = arr[0]
end = arr[0] + l
cnt = 1
for i in range(n):
    if start <= arr[i] < end:
        continue
    else:
        start = arr[i]
        end = arr[i] + l
        cnt += 1
print(cnt)
