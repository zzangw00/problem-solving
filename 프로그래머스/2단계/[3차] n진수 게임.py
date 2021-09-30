def change(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return change(q, base) + T[r]


def solution(n, t, m, p):
    answer = ''
    a = -1
    modeBit = 0
    cnt = 1
    stack = []
    while modeBit == 0:
        a += 1
        temp = list(change(a, n))
        for i in range(len(temp)):
            if cnt == p:
                answer += temp[i]
                if len(answer) == t:
                    modeBit = 1
                    break
                cnt += 1
            else:
                stack.append(temp[i])
                cnt += 1
            if cnt > m:
                cnt = 1

    return answer
