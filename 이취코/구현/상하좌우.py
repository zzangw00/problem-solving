n = int(input())
arr = input().split()
x, y = 1, 1
data = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in arr:
    for j in range(4):
        if i == data[j]:
            newX = x + dx[j]
            newY = y + dy[j]
            if newX < 1 or newY < 1 or newX > n or newY > n:
                continue
            else:
                x = newX
                y = newY

print(x, y)
