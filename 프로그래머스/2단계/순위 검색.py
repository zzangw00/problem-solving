from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    dic = {}
    comb = [0, 1, 2, 3]
    for i in info:
        person = i.split()
        conditions = person[:-1]
        score = int(person[-1])
        for j in range(5):
            for k in list(combinations(comb, j)):
                temp = conditions.copy()
                for idx in k:
                    temp[idx] = '-'
                key = ''.join(temp)
                if key in dic:
                    dic[key].append(score)
                else:
                    dic[key] = [score]
    for value in dic.values():
        value.sort()
    for i in query:
        q_list = []
        for j in i.split():
            if j == 'and':
                continue
            q_list.append(j)

        target = int(q_list[-1])
        key = ''.join(q_list[:-1])

        if key in dic:
            hubo_list = dic[key]

            index = bisect_left(hubo_list, target)
            answer.append(len(hubo_list) - index)
        else:
            answer.append(0)
            continue
    return answer
