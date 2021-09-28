dd = [[[-1, 0], [-1, 1], [0, 1]], [[0, 1], [1, 1], [1, 0]],
      [[1, 0], [1, -1], [0, -1]], [[0, -1], [-1, -1], [-1, 0]]]


def check(x, y, board2, visited):
    temp = []
    for i in dd:
        temp2 = []
        for j in i:
            nx = x + j[0]
            ny = y + j[1]
            if nx < 0 or nx >= len(board2) or ny < 0 or ny >= len(board2[0]):
                continue
            else:
                if board2[nx][ny] == board2[x][y]:
                    temp2.append([nx, ny])
                else:
                    temp2 = []
        if len(temp2) == 3:
            temp = temp2
    if temp:
        for i in temp:
            visited[i[0]][i[1]] = 1
        visited[x][y] = 1
    return temp


def change(board2, visited):
    cnt = 0
    for i in range(len(board2)):
        for j in range(len(board2[0])):
            a = visited[i][j]
            if a == 1:
                board2[i][j] = 0
                cnt += 1
    return cnt


def down(board2):
    temp = []
    for i in range(len(board2[0])):
        temp.append([])
    for i in range(len(board2[0])):
        for j in range(len(board2) - 1, -1, -1):
            if board2[j][i] != 0:
                temp[i].append(board2[j][i])
    for i in range(len(temp)):
        for j in range(len(board2) - len(temp[i])):
            temp[i].append(0)
    return temp


def solution(m, n, board):
    answer = 0
    visited = [[0 for _ in range(n)] for _ in range(m)]
    board2 = []
    for i in range(m):
        board2.append([])
    for i in range(m):
        for j in range(n):
            board2[i].append(board[i][j])
    while True:
        for i in range(m):
            for j in range(n):
                if board2[i][j] != 0:
                    check(i, j, board2, visited)
        a = change(board2, visited)
        visited = [[0 for _ in range(n)] for _ in range(m)]
        answer += a
        if a == 0:
            break
        b = down(board2)
        for i in range(len(b[0]) - 1, -1, -1):
            for j in range(len(b)):
                board2[i][j] = b[j][i]
        board2.reverse()
    return answer
