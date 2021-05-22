n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 1

for i in arr:
    if i > result:
        break
    result += i

print(result)
