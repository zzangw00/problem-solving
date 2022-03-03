from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


def solution(arr):
    answer = 0
    queue = deque()
    arr.sort(reverse=True)
    for i in range(len(arr)):
        queue.append(arr[i])

    while len(queue) > 1:
        if len(queue) >= 2:
            a = queue[0]
            if a >= 0:
                a = queue.popleft()
            else:
                break
            b = queue[0]
            if a > 0:
                if a * b <= 0:
                    answer += a
                else:
                    if b == 1:
                        answer += a
                    else:
                        b = queue.popleft()
                        answer += (a * b)
            else:
                b = queue.popleft()
                answer += (a * b)

    while len(queue) > 1:
        if len(queue) >= 2:
            a = queue.pop()
            b = queue.pop()
            answer += (a * b)

    if len(queue) > 0:
        answer += queue.popleft()
    return answer


print(solution(arr))
