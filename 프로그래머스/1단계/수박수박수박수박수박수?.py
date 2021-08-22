def solution(n):
    answer = ''
    if n % 2 == 0:
        for i in range(n // 2):
            answer += '수박'
    else:
        for i in range(n // 2):
            answer += '수박'
        answer += '수'
    return answer
