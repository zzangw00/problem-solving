n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = 0
y = 0
answer = []
while True:
    if x == n or y == m:
        break
    if a[x] > b[y]:
        answer.append(b[y])
        y += 1
    else:
        answer.append(a[x])
        x += 1
if x != n:
    for i in range(x, n):
        answer.append(a[i])
else:
    for i in range(y, m):
        answer.append(b[i])

print(' '.join(map(str, answer)))
