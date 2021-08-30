import math


def solution(n, a, b):
    answer = 0
    cnt = 0
    for i in range(n // 2):
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        cnt += 1
        if a == b:
            answer = cnt
            break

    return answer
