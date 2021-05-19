n, m = map(int, input().split())
resultArr = []
for i in range(n):
    arr = list(map(int, input().split()))
    resultArr.append(min(arr))

print(max(resultArr))