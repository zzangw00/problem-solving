def solution(n):
    answer = 0

    b = format(n, 'b')
    result = str(b)
    answer = result.count("1")
    return answer
