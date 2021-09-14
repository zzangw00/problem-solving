import sys
n = int(input())
m = int(input())
arr = []
answer = []
result = []
for i in range(n + 1):
    arr.append([])
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

a = arr[1]
for i in a:
    answer.append(arr[i])
for i in answer:
    for j in i:
        result.append(j)
for i in a:
    result.append(i)
if result:
    print(len(set(result)) - 1)
else:
    print(0)
