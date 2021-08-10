def solution(arr):
    answer = []
    minResult = min(arr)
    if len(arr) > 1:
        for i in arr:
            if i != minResult:
                answer.append(i)
    else:
        answer.append(-1)
    return answer
