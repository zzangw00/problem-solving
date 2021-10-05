from collections import defaultdict


def solution(table, languages, preference):
    answer = ''
    dic = defaultdict(int)
    for i in table:
        a = i.split()
        target = a[0]
        for j in range(1, len(a)):
            if a[j] in languages:
                b = preference[languages.index(a[j])]
                dic[target] += (b * (6 - a.index(a[j])))
    answer = max(dic, key=dic.get)
    result = list(zip(dic.keys(), dic.values()))
    result = sorted(result, key=lambda x: (-x[1], x[0]))
    answer = result[0][0]
    return answer
