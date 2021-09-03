def solution(dirs):
    answer = 0
    arr = list(dirs)
    graph = [[0] * 11 for _ in range(11)]
    data = ['L', 'R', 'U', 'D']
    path = []
    graph[5][5] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    x = 5
    y = 5
    for i in range(len(arr)):
        for j in range(4):
            if arr[i] == data[j]:
                nx = x + dx[j]
                ny = y + dy[j]
                a = {(nx, ny), (x, y)}
                if nx < 0 or ny < 0 or nx > 10 or ny > 10:
                    continue
                else:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        path.append(a)
                        x = nx
                        y = ny
                        answer += 1
                    else:
                        if a in path:
                            x = nx
                            y = ny
                        else:
                            path.append(a)
                            x = nx
                            y = ny
                            answer += 1
    return answer
