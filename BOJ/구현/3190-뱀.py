from collections import deque
n = int(input())
k = int(input())
apple = []
vector = deque()
answer = 0
for _ in range(k):
    apple.append(list(map(int, input().split(' '))))
l = int(input())
for _ in range(l):
    vector.append(list(input().split(' ')))
v = 1  # 현재 방향
dx = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dy = [0, 1, 0, -1]
queue = deque()
queue.append([0, 0])
for i in range(1, 10000):
    nx = queue[-1][0] + dx[v]
    ny = queue[-1][1] + dy[v]
    if nx >= n or ny >= n or nx < 0 or ny < 0:
        answer = i
        break
    if [nx, ny] in queue:
        answer = i
        break
    else:
        if [nx + 1, ny + 1] in apple:
            apple.remove([nx + 1, ny + 1])
            queue.append([nx, ny])
        else:
            queue.append([nx, ny])
            queue.popleft()
    if vector:
        if i == int(vector[0][0]):
            if vector[0][1] == 'D':
                vector.popleft()
                v += 1
                if v > 3:
                    v = 0
            else:
                vector.popleft()
                v -= 1
                if v < 0:
                    v = 3
print(answer)
