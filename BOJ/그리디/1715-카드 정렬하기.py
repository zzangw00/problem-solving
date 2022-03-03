import heapq

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
heapq.heapify(arr)


def solution(arr):
    answer = 0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        answer += (a + b)
        heapq.heappush(arr, a + b)

    return answer


print(solution(arr))
