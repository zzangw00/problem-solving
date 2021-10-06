def solution(scores):
    answer = ''
    board = []
    scores2 = []
    for i in range(len(scores)):
        scores2.append([])
    for i in range(len(scores[0])):
        for j in range(len(scores)):
            scores2[i].append(scores[j][i])
    for i in range(len(scores2)):
        if scores2[i][i] == min(scores2[i]) and scores2[i].count(scores2[i][i]) == 1:
            scores2[i].remove(scores2[i][i])
            board.append(sum(scores2[i]) / len(scores2[i]))
            continue
        if scores2[i][i] == max(scores2[i]) and scores2[i].count(scores2[i][i]) == 1:
            scores2[i].remove(scores2[i][i])
            board.append(sum(scores2[i]) / len(scores2[i]))
            continue
        board.append(sum(scores2[i]) / len(scores2[i]))
    for i in board:
        if i >= 90:
            answer += 'A'
        elif i >= 80 and i < 90:
            answer += 'B'
        elif i < 80 and i >= 70:
            answer += 'C'
        elif i < 70 and i >= 50:
            answer += 'D'
        elif i < 50:
            answer += 'F'
    return answer
