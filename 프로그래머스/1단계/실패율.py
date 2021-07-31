def solution(N, stages):
    answer = []
    score = []
    R = len(stages)
    for i in range(1, N + 1):
        if R != 0:
            count = stages.count(i)
            score.append((i, count / R))
            R -= count
        else:
            score.append((i, 0))

    score = sorted(score, key=lambda x: (-x[1], x[0]))
    for i in range(len(score)):
        answer.append(score[i][0])
    return answer
