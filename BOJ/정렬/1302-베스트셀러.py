n = int(input())
arr = []
result = []
for i in range(n):
    arr.append(input())

for i in arr:
    result.append((i, arr.count(i)))

answer = sorted(result, key=lambda x: (-x[1], x[0]))

print(answer[0][0])
