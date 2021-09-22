from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = deque()
for i in range(n):
    a = input().strip().split(' ')
    if len(a) == 2:
        if a[0] == 'push_front':
            arr.appendleft(int(a[1]))
        else:
            arr.append(int(a[1]))
    else:
        if a[0] == 'pop_front':
            if arr:
                print(arr.popleft())
            else:
                print(-1)
        if a[0] == 'pop_back':
            if arr:
                print(arr.pop())
            else:
                print(-1)
        if a[0] == 'size':
            print(len(arr))
        if a[0] == 'empty':
            if arr:
                print(0)
            else:
                print(1)
        if a[0] == 'front':
            if arr:
                print(arr[0])
            else:
                print(-1)
        if a[0] == 'back':
            if arr:
                print(arr[-1])
            else:
                print(-1)
