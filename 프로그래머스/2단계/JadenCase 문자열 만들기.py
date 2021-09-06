def solution(s):
    answer = ''
    s = s.lower()
    arr = s.split(' ')
    for i in arr:
        i = i.capitalize()
        answer += i + ' '

    return answer[:-1]
