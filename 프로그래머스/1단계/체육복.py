def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n + 1):
        if i not in lost:
            answer += 1
            continue
        if i in lost and i in reserve:
            answer += 1
            reserve.remove(i)
            continue
        if i in lost:
            if i - 1 in reserve:
                answer += 1
                reserve.remove(i - 1)
                continue
            if i + 1 in reserve:
                if i + 1 in lost:
                    continue
                else:
                    answer += 1
                    reserve.remove(i + 1)
                continue
    return answer
