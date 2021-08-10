def solution(n):
    answer = 0
    arr = list(str(n))
    arr = list(map(int, arr))
    result = sorted(arr, key=lambda x: -x)
    result = list(map(str, result))
    answer = ''.join(result)
    return int(answer)
