n = int(input())
visited = []
for _ in range(100):
    visited.append([0] * 100)
dragon = []
for _ in range(n):
    dragon.append(list(map(int, input().split())))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def solution():
    for i in range(n):
        x, y, d, g = dragon[i]
        move = []
        move.append(d)
        for i in range(g):
            temp = []
            for j in range(len(move) - 1, -1, -1):
                temp.append((move[j] + 1) % 4)
            move += temp
        check(x, y, move)


def check(x, y, move):
    global visited
    visited[x][y] = 1
    for i in range(len(move)):
        d = move[i]
        x += dx[d]
        y += dy[d]
        visited[x][y] = 1


answer = 0

solution()
for x in range(99):
    for y in range(99):
        if visited[x][y] == 1 and visited[x][y + 1] == 1 and visited[x + 1][y + 1] == 1 and visited[x + 1][y] == 1:
            answer += 1
print(answer)
