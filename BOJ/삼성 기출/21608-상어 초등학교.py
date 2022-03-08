import copy

n = int(input())
arr = []
for _ in range(n ** 2):
    arr.append(list(map(int, input().split())))
graph = []  # 실제 들어가는 학생 넣는 그래프
for i in range(n):
    graph.append([0] * n)
graph2 = []
for i in range(n):
    graph2.append([-1] * n)


def solution(arr, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 0
    for i in range(len(arr)):
        a = arr[i][0]
        v = []
        v2 = []
        v3 = []
        v4 = []
        check = copy.deepcopy(graph2)  # 인접한 학생이 몇명 있는지 체크하기위한 그래프
        check2 = copy.deepcopy(graph2)
        for x in range(len(check)):
            for y in range(len(check[x])):
                cnt = 0
                cnt2 = 0
                if graph[x][y] == 0:
                    for j in range(4):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if nx >= len(graph) or nx < 0 or ny >= len(graph) or ny < 0:
                            continue
                        else:
                            for k in range(1, 5):
                                if graph[nx][ny] == arr[i][k]:
                                    cnt += 1
                                if graph[nx][ny] == 0:
                                    cnt2 += 1
                    check[x][y] = cnt
                    check2[x][y] = cnt2
        for x in range(len(check)):
            for y in range(len(check[x])):
                if not v:
                    v.append([x, y])
                else:
                    if check[x][y] > check[v[-1][0]][v[-1][1]]:
                        v = [[x, y]]
                    if check[x][y] == check[v[-1][0]][v[-1][1]]:
                        v.append([x, y])
        if len(v) > 1:
            for j in range(len(v)):
                if not v2:
                    v2.append([v[j][0], v[j][1]])
                else:
                    if check2[v[j][0]][v[j][1]] > check2[v2[-1][0]][v2[-1][1]]:
                        v2 = [[v[j][0], v[j][1]]]
                    if check2[v[j][0]][v[j][1]] == check2[v2[-1][0]][v2[-1][1]]:
                        v2.append([v[j][0], v[j][1]])
            if len(v2) > 1:
                for k in range(len(v2)):
                    if not v3:
                        v3.append([v2[k][0], v2[k][1]])
                    else:
                        if v2[k][0] < v3[-1][0]:
                            v3 = [[v2[k][0], v2[k][1]]]
                        if v2[k][0] == v3[-1][0]:
                            v3.append([v2[k][0], v2[k][1]])
                if len(v3) > 1:
                    for t in range(len(v3)):
                        if not v4:
                            v4.append([v3[t][0], v3[t][1]])
                        else:
                            if v3[t][1] < v4[-1][1]:
                                v4 = [[v3[t][0], v3[t][1]]]
                            if v3[t][0] == v4[-1][1]:
                                v4.append([v3[t][0], v3[t][1]])
                    graph[v4[0][0]][v4[0][1]] = a
                else:
                    graph[v3[0][0]][v3[0][1]] = a
            else:
                graph[v2[0][0]][v2[0][1]] = a

        else:
            graph[v[0][0]][v[0][1]] = a

    for x in range(len(graph)):
        for y in range(len(graph[x])):
            a = graph[x][y]
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= len(graph) or nx < 0 or ny >= len(graph) or ny < 0:
                    continue
                else:
                    for j in range(len(arr)):
                        if a == arr[j][0]:
                            for k in range(1, 5):
                                if graph[nx][ny] == arr[j][k]:
                                    cnt += 1
            if cnt == 0:
                answer += 0
            else:
                answer += (10 ** (cnt - 1))
    return answer


print(solution(arr, graph))
