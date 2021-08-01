def solution(s):
    answer = ''
    arr = list(s)
    if len(arr) % 2 == 1:
        answer += arr[len(arr) // 2]
    else:
        answer += arr[(len(arr) // 2) - 1]
        answer += arr[len(arr) // 2]
    return answer
