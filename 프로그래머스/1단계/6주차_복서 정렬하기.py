def solution(weights, head2head):
    answer = []
    result = []
    for i in range(len(weights)):
        result.append([])
    for i in range(len(head2head)):
        cnt = 0
        bigWin = 0
        nCount = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W':
                cnt += 1
            if head2head[i][j] == 'W' and weights[i] < weights[j]:
                bigWin += 1
            if head2head[i][j] == 'N':
                nCount += 1
        if cnt == 0:
            result[i].append(0)
        else:
            result[i].append(100 * (cnt / (len(head2head[i]) - nCount)))
        result[i].append(bigWin)
        result[i].append(weights[i])
        result[i].append(i + 1)
    result = sorted(result, key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    for i in range(len(result)):
        answer.append(result[i][3])

    return answer
