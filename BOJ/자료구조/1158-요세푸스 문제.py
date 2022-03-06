from collections import deque

n, k = map(int, input().split(' '))
queue = []
queue = deque()
for i in range(n):
    queue.append(i + 1)


def solution(queue, k):
    answer = []
    cnt = 0
    while queue:
        a = queue.popleft()
        cnt += 1
        if cnt == k:
            cnt = 0
            answer.append(a)
        else:
            queue.append(a)
    return answer


a = solution(queue, k)
print("<", end='')
print(', '.join(map(str, a)) + ">")
