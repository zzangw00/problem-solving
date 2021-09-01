def solution(s):
    answer = []
    arr = list(map(int, s.split()))
    answer.append(min(arr))
    answer.append(max(arr))
    result = list(map(str, answer))

    return ' '.join(result)
