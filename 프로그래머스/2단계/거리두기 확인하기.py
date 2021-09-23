dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def second(a, arr, x, y):
    result = 1
    q = 0
    for i in range(len(a)):
        for j in range(4):
            nx = a[i][0] + dx[j]
            ny = a[i][1] + dy[j]
            if nx >= 5 or ny >= 5 or nx < 0 or ny < 0:
                continue
            elif nx == x and ny == y:
                continue
            else:
                if arr[nx][ny] == 'P':
                    q = 1
    if q == 1:
        result = 0
    else:
        result = 1
    return result


def first(x, y, arr):
    queue = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 5 or ny >= 5 or nx < 0 or ny < 0:
            continue
        else:
            if arr[nx][ny] == 'O':
                queue.append([nx, ny])
            if arr[nx][ny] == 'P':
                queue = 0
                break
    return queue


def solution(places):
    answer = []
    for k in range(len(places)):
        z = 0
        v = 1
        for i in range(len(places[k])):
            for j in range(len(places[k][i])):
                if places[k][i][j] == 'P':
                    a = first(i, j, places[k])
                    if a == 0:
                        z = 1
                    else:
                        if a:
                            b = second(a, places[k], i, j)
                            if b == 0:
                                z = 1
        if z == 1:
            answer.append(0)
        else:
            answer.append(v)

    return answer
