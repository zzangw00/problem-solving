def solution(s):
    answer = ''
    arr = list(s)
    arr = sorted(arr, reverse=True)
    answer = ''.join(arr)
    return answer
