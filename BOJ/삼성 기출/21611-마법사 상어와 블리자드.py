n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
move = []
for _ in range(m):
    o, u = map(int, input().split())
    move.append([o - 1, u])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dx2 = [0, 1, 0, -1]
dy2 = [-1, 0, 1, 0]
answer = 0


def solution():
    for i in range(m):
        attack(move[i])
        arr = fill()
        arr2 = four(arr)
        arr3 = jjack(arr2)
        fill2(arr3)
    return answer


def attack(k):
    global graph, answer
    x = n // 2
    y = n // 2
    d, p = k
    for _ in range(p):
        nx = x + dx[d]
        ny = y + dy[d]
        graph[nx][ny] = 0
        x = nx
        y = ny


def fill():
    x = n // 2
    y = n // 2
    d = 0
    cnt = 0
    cnt2 = 0
    flag = 1
    stack = []
    while True:
        nx = x + dx2[d]
        ny = y + dy2[d]
        cnt += 1
        if cnt == flag:
            cnt2 += 1
            cnt = 0
            d = (d + 1 + 4) % 4
        if cnt2 == 2:
            cnt2 = 0
            flag += 1
        if graph[nx][ny] != 0:
            stack.append(graph[nx][ny])
        x = nx
        y = ny
        if x == 0 and y == 0:
            break
    return stack


def four(arr):
    global answer
    while True:
        stack = []
        cnt = 1
        flag = 0
        for i in range(len(arr)):
            if not stack:
                stack.append(arr[i])
            else:
                if stack[-1] == arr[i]:
                    cnt += 1
                    stack.append(arr[i])
                else:
                    if cnt >= 4:
                        for _ in range(cnt):
                            a = stack.pop()
                            answer += a
                        flag = 1
                        cnt = 1
                        stack.append(arr[i])
                    else:
                        cnt = 1
                        stack.append(arr[i])
        if cnt >= 4:
            for _ in range(cnt):
                a = stack.pop()
                answer += a
        arr = stack
        if flag == 0:
            break
    return arr


def jjack(arr):
    stack = []
    stack2 = []
    for i in range(len(arr)):
        if not stack:
            stack.append(arr[i])
        else:
            if stack[-1] == arr[i]:
                stack.append(arr[i])
            else:
                stack2.append(len(stack))
                stack2.append(stack[-1])
                stack = []
                stack.append(arr[i])
    if stack:
        stack2.append(len(stack))
        stack2.append(stack[-1])

    return stack2


def fill2(arr):
    global graph
    new = []
    for _ in range(n):
        new.append([0] * n)
    x = n // 2
    y = n // 2
    d = 0
    cnt = 0
    cnt2 = 0
    flag = 1
    for i in range(len(arr)):
        nx = x + dx2[d]
        ny = y + dy2[d]
        cnt += 1
        if cnt == flag:
            cnt = 0
            cnt2 += 1
            d = (d + 1 + 4) % 4
        if cnt2 == 2:
            cnt2 = 0
            flag += 1
        new[nx][ny] = arr[i]
        x = nx
        y = ny
        if x == 0 and y == 0:
            break
    graph = new


print(solution())
