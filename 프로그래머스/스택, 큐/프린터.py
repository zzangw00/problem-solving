from collections import deque


def solution(priorities, location):
    answer = 0
    cnt = 0
    queue = deque()
    queue2 = deque()
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
        queue2.append(priorities[i])
    while queue:
        if queue2[0] is not max(queue2):
            a, idx = queue.popleft()
            queue.append((a, idx))
            b = queue2.popleft()
            queue2.append(b)
        else:
            b = queue2.popleft()
            a, idx = queue.popleft()
            cnt += 1
            if idx == location:
                answer = cnt
    return answer
