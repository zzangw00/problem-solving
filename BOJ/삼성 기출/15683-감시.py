from itertools import product
import copy
from re import T

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def solution(graph):
    answer = 1000000
    arr = []
    temp = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            if graph[x][y] != 0 and graph[x][y] != 6:
                arr.append([graph[x][y], x, y])
    for i in range(len(arr)):
        if arr[i][0] == 1:
            temp.append([1, 2, 3, 4])
        if arr[i][0] == 2:
            temp.append([1, 2])
        if arr[i][0] == 3:
            temp.append([1, 2, 3, 4])
        if arr[i][0] == 4:
            temp.append([1, 2, 3, 4])
        if arr[i][0] == 5:
            temp.append([1])
    items = list(product(*temp))
    for i in range(len(items)):
        cnt2 = 0
        cctv = copy.deepcopy(graph)
        for j in range(len(arr)):
            a, x, y = arr[j]
            while True:
                if a == 1:
                    fx = x
                    fy = y
                    if items[i][j] == 1:
                        ny = y + dy[3]
                        if ny >= len(graph[0]) or cctv[x][ny] == 6:
                            y = fy
                            break
                        else:
                            if cctv[x][ny] == 0:
                                cctv[x][ny] = 7
                                y = ny
                            else:
                                y = ny
                    if items[i][j] == 2:
                        nx = x + dx[0]
                        if nx < 0 or cctv[nx][y] == 6:
                            x = fx
                            break
                        else:
                            if cctv[nx][y] == 0:
                                cctv[nx][y] = 7
                                x = nx
                            else:
                                x = nx
                    if items[i][j] == 3:
                        ny = y + dy[2]
                        if ny < 0 or cctv[x][ny] == 6:
                            y = fy
                            break
                        else:
                            if cctv[x][ny] == 0:
                                cctv[x][ny] = 7
                                y = ny
                            else:
                                y = ny
                    if items[i][j] == 4:
                        nx = x + dx[1]
                        if nx >= len(graph) or cctv[nx][y] == 6:
                            x = fx
                            break
                        else:
                            if cctv[nx][y] == 0:
                                cctv[nx][y] = 7
                                x = nx
                            else:
                                x = nx
                if a == 2:
                    cnt = 0
                    fx = x
                    fy = y
                    if items[i][j] == 1:
                        for k in range(2):
                            while True:
                                if k == 0:
                                    ny = y + dy[3]
                                    if ny >= len(graph[0]) or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                                if k == 1:
                                    ny = y + dy[2]
                                    if ny < 0 or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                            cnt += 1
                        if cnt == 2:
                            cnt = 0
                            break
                    if items[i][j] == 2:
                        for k in range(2):
                            while True:
                                if k == 0:
                                    nx = x + dx[0]
                                    if nx < 0 or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                                if k == 1:
                                    nx = x + dx[1]
                                    if nx >= len(graph) or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                            cnt += 1
                        if cnt == 2:
                            cnt = 0
                            break
                if a == 3:
                    fx = x
                    fy = y
                    cnt = 0
                    if items[i][j] == 1:
                        for k in range(2):
                            while True:
                                if k == 0:
                                    ny = y + dy[3]
                                    if ny >= len(graph[0]) or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                                if k == 1:
                                    nx = x + dx[0]
                                    if nx < 0 or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                            cnt += 1
                        if cnt == 2:
                            cnt = 0
                            break
                    if items[i][j] == 2:
                        for k in range(2):
                            while True:
                                if k == 0:
                                    nx = x + dx[0]
                                    if nx < 0 or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                                if k == 1:
                                    ny = y + dy[2]
                                    if ny < 0 or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                            cnt += 1
                        if cnt == 2:
                            cnt = 0
                            break
                    if items[i][j] == 3:
                        for k in range(2):
                            while True:
                                if k == 0:
                                    ny = y + dy[2]
                                    if ny < 0 or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                                if k == 1:
                                    nx = x + dx[1]
                                    if nx >= len(graph) or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                            cnt += 1
                        if cnt == 2:
                            cnt = 0
                            break
                    if items[i][j] == 4:
                        for k in range(2):
                            while True:
                                if k == 0:
                                    ny = y + dy[3]
                                    if ny >= len(graph[0]) or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                                if k == 1:
                                    nx = x + dx[1]
                                    if nx >= len(graph) or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                            cnt += 1
                        if cnt == 2:
                            cnt = 0
                            break
                if a == 4:
                    fx = x
                    fy = y
                    cnt = 0
                    if items[i][j] == 1:
                        for k in range(3):
                            while True:
                                if k == 0:
                                    ny = y + dy[3]
                                    if ny >= len(graph[0]) or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                                if k == 1:
                                    nx = x + dx[0]
                                    if nx < 0 or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                                if k == 2:
                                    ny = y + dy[2]
                                    if ny < 0 or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                            cnt += 1
                        if cnt == 3:
                            cnt = 0
                            break
                    if items[i][j] == 2:
                        for k in range(3):
                            while True:
                                if k == 0:
                                    nx = x + dx[0]
                                    if nx < 0 or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                                if k == 1:
                                    ny = y + dy[2]
                                    if ny < 0 or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                                if k == 2:
                                    nx = x + dx[1]
                                    if nx >= len(graph) or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                            cnt += 1
                        if cnt == 3:
                            cnt = 0
                            break
                    if items[i][j] == 3:
                        for k in range(3):
                            while True:
                                if k == 0:
                                    ny = y + dy[2]
                                    if ny < 0 or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                                if k == 1:
                                    nx = x + dx[1]
                                    if nx >= len(graph) or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                                if k == 2:
                                    ny = y + dy[3]
                                    if ny >= len(graph[0]) or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                            cnt += 1
                        if cnt == 3:
                            cnt = 0
                            break
                    if items[i][j] == 4:
                        for k in range(3):
                            while True:
                                if k == 0:
                                    nx = x + dx[1]
                                    if nx >= len(graph) or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                                if k == 1:
                                    ny = y + dy[3]
                                    if ny >= len(graph[0]) or cctv[x][ny] == 6:
                                        y = fy
                                        break
                                    else:
                                        if cctv[x][ny] == 0:
                                            cctv[x][ny] = 7
                                            y = ny
                                        else:
                                            y = ny
                                if k == 2:
                                    nx = x + dx[0]
                                    if nx < 0 or cctv[nx][y] == 6:
                                        x = fx
                                        break
                                    else:
                                        if cctv[nx][y] == 0:
                                            cctv[nx][y] = 7
                                            x = nx
                                        else:
                                            x = nx
                            cnt += 1
                        if cnt == 3:
                            cnt = 0
                            break
                if a == 5:
                    fx = x
                    fy = y
                    cnt = 0
                    for k in range(4):
                        while True:
                            if k == 0:
                                nx = x + dx[0]
                                if nx < 0 or cctv[nx][y] == 6:
                                    x = fx
                                    break
                                else:
                                    if cctv[nx][y] == 0:
                                        cctv[nx][y] = 7
                                        x = nx
                                    else:
                                        x = nx
                            if k == 1:
                                ny = y + dy[3]
                                if ny >= len(graph[0]) or cctv[x][ny] == 6:
                                    y = fy
                                    break
                                else:
                                    if cctv[x][ny] == 0:
                                        cctv[x][ny] = 7
                                        y = ny
                                    else:
                                        y = ny
                            if k == 2:
                                nx = x + dx[1]
                                if nx >= len(graph) or cctv[nx][y] == 6:
                                    x = fx
                                    break
                                else:
                                    if cctv[nx][y] == 0:
                                        cctv[nx][y] = 7
                                        x = nx
                                    else:
                                        x = nx
                            if k == 3:
                                ny = y + dy[2]
                                if ny < 0 or cctv[x][ny] == 6:
                                    y = fy
                                    break
                                else:
                                    if cctv[x][ny] == 0:
                                        cctv[x][ny] = 7
                                        y = ny
                                    else:
                                        y = ny
                        cnt += 1
                    if cnt == 4:
                        cnt = 0
                        break

        for x in range(len(cctv)):
            for y in range(len(cctv[0])):
                if cctv[x][y] == 0:
                    cnt2 += 1
        answer = min(answer, cnt2)

    return answer


print(solution(graph))
