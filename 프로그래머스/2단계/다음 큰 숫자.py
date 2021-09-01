def solution(n):
    answer = 0
    arr = list(format(n, 'b'))
    cnt = arr.count("1")
    for i in range(n + 1, 1000001):
        arr2 = list(format(i, 'b'))
        cnt2 = arr2.count("1")
        if cnt2 == cnt:
            answer = i
            break

    return answer
