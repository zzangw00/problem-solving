n, k = map(int, input().split())
arr = []
count = 0

for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

for i in arr:
    if k == 0:
        break
    count = count + (k // i)
    k = k % i
print(count)
