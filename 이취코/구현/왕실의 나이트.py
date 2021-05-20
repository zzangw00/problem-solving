data = input()
count = 0
x = int(ord(data[0])) - int(ord('a')) + 1
y = int(data[1])

move = [[2, -1], [2, 1], [-2, -1], [-2, 1], [1, -2], [1, 2], [-1, -2], [-1, 2]]

for i in move:
    nx = x + i[0]
    ny = y + i[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        count += 1

print(count)