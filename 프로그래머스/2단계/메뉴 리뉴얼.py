from itertools import combinations


def solution(orders, course):
    answer = []
    temp = []
    for i in range(len(orders)):
        for j in range(len(course)):
            arr = list(combinations(orders[i], course[j]))
            if arr:
                for k in arr:
                    a = list(k)
                    a.sort()
                    temp.append(a)
    for j in range(len(course)):
        temp2 = []
        temp3 = []
        for i in range(len(temp)):
            if len(temp[i]) == course[j]:
                if temp.count(temp[i]) >= 2:
                    temp2.append((tuple(set(temp[i])), temp.count(temp[i])))
        a = set(temp2)
        a = sorted(a, key=lambda x: -x[1])
        if a:
            temp3.append(a[0])
        if len(a) >= 2:
            for i in range(1, len(a)):
                if a[i][1] == temp3[0][1]:
                    temp3.append(a[i])
                else:
                    break
        for i in temp3:
            x = list(i[0])
            x.sort()
            answer.append(''.join(x))
    answer.sort()
    return answer
