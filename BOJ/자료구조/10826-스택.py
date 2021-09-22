import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    a = input().strip().split()
    if len(a) == 2:
        stack.append(int(a[1]))
    else:
        if a[0] == 'pop':
            if stack:
                s = stack.pop()
                print(s)
            else:
                print(-1)
        if a[0] == 'size':
            print(len(stack))
        if a[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        if a[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
