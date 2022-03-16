n, m, x, y, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
move = list(map(int, input().split()))


def solution(graph, move, x, y):
    dice = [0] * 7
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    for i in range(len(move)):
        nx = x + dx[move[i]]
        ny = y + dy[move[i]]
        if nx >= len(graph) or nx < 0 or ny >= len(graph[0]) or ny < 0:
            continue
        else:
            if move[i] == 1:
                dice[4], dice[6], dice[3], dice[1] = dice[6], dice[3], dice[1], dice[4]
            elif move[i] == 2:
                dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
            elif move[i] == 3:
                dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
            else:
                dice[2], dice[6], dice[5], dice[1] = dice[6], dice[5], dice[1], dice[2]

            if graph[nx][ny] == 0:
                graph[nx][ny] = dice[6]
            else:
                dice[6] = graph[nx][ny]
                graph[nx][ny] = 0
            x = nx
            y = ny
            print(dice[1])


solution(graph, move, x, y)
