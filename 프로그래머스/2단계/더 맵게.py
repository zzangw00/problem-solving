import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    for i in range(len(scoville)):
        a = heapq.heappop(scoville)
        if a >= K:
            heapq.heappush(scoville, a)
            break
        b = heapq.heappop(scoville)
        c = a + (b * 2)
        heapq.heappush(scoville, c)
        if len(scoville) == 1:
            if scoville[0] < K:
                answer = -1
                break
        answer += 1

    return answer
