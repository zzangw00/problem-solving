import sys

n = int(input())

for i in range(n):
    t = int(input())
    arr = []
    cnt = 1
    for j in range(t):
        arr.append(list(map(int, sys.stdin.readline().split())))
    arr.sort()
    temp = arr[0][1]
    for k in range(1, t):
        if arr[k][1] < temp:
            cnt += 1
            temp = arr[k][1]
    print(cnt)
