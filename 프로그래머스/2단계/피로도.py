from itertools import permutations


def solution(k, dungeons):
    answer = -1
    items = list(permutations(dungeons, len(dungeons)))
    for i in range(len(items)):
        cnt = 0
        temp = k
        for j in range(len(items[i])):
            if items[i][j][0] <= temp:
                temp -= items[i][j][1]
                cnt += 1
        answer = max(answer, cnt)
    return answer
