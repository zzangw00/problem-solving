def solution(n):
    answer = 0
    for i in range(1, n + 1):
        sumOfNum = 0
        for j in range(i, n + 1):
            sumOfNum += j
            if sumOfNum == n:
                answer += 1
                break
            if sumOfNum > n:
                break
    return answer
