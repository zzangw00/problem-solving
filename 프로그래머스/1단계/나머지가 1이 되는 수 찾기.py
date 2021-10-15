def solution(n):
    answer = n
    for i in range(n, 0, -1):
        if n % i == 1:
            if i < answer:
                answer = i
    return answer
