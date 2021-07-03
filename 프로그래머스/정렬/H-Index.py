def solution(citations):
    answer = 0
    citations.sort()
    for i in range(max(citations)):
        cnt = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                cnt += 1
            if cnt >= i and len(citations) - cnt <= i:
                answer = max(i, answer)
    return answer
