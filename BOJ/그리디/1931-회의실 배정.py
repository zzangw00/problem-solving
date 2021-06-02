n = int(input())
arr = []
count = 1
for i in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key=lambda x: (x[1], x[0]))
last = arr[0]
for i in range(1, n):
    if arr[i][0] >= last[1]:
        count += 1
        last = arr[i]

print(count)
