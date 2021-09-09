def solution(s):
    answer = []
    arr = list(s)
    cnt0 = 0
    cnt = 0
    while len(arr) > 1:
        a = len(arr)
        arr = [item for item in arr if item != '0']
        cnt0 += (a - len(arr))
        arr = list(format(len(arr), 'b'))
        cnt += 1

    answer.append(cnt)
    answer.append(cnt0)
    return answer
