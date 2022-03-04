import heapq

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split(' '))))
arr.sort()


def solution(arr):
    room = []
    heapq.heappush(room, arr[0][1])
    for i in range(1, len(arr)):
        if room[0] > arr[i][0]:
            heapq.heappush(room, arr[i][1])
        else:
            heapq.heappop(room)
            heapq.heappush(room, arr[i][1])
    return len(room)


print(solution(arr))
