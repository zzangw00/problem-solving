from sys import stdin

queue = []

for _ in range(int(stdin.readline())):
    arr = stdin.readline().split()
    if arr[0] == 'push':
        queue.append(arr[1])

    elif arr[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)

    elif arr[0] == 'size':
        print(len(queue))

    elif arr[0] == 'empty':
        print(1 - int(bool(queue)))

    elif arr[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif arr[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        continue
