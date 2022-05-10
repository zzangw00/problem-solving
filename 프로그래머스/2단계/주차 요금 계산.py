import math
from collections import defaultdict


def solution(fees, records):
    answer = []
    dic = defaultdict(list)
    dic2 = defaultdict(int)
    dic3 = defaultdict(int)
    for i in range(len(records)):
        arr = records[i].split()
        dic[arr[1]].append(arr[0])
    for i in dic:
        for j in range(len(dic[i])):
            a = dic[i][j]
            b = a.split(':')
            c = int(b[0]) * 60
            d = int(b[1])
            dic[i][j] = c + d
    for i in dic:
        if len(dic[i]) % 2 == 1:
            dic[i].append(23 * 60 + 59)
    for i in dic:
        for j in range(1, len(dic[i]), 2):
            dic2[i] += (dic[i][j] - dic[i][j - 1])
    for i in dic2:
        if dic2[i] <= fees[0]:
            dic3[i] = fees[1]
        else:
            dic3[i] = fees[1] + \
                (math.ceil((dic2[i] - fees[0]) / fees[2]) * fees[3])
    result = []
    for i in dic3:
        result.append([i, dic3[i]])
    result = sorted(result, key=lambda x: x[0])
    for i in result:
        answer.append(i[1])
    return answer
