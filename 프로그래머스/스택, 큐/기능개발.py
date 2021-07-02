from collections import deque


def solution(progresses, speeds):
    answer = []
    cnt = 0
    days = 0
    queue = deque()
    speedQueue = deque()
    for i in range(len(progresses)):
        queue.append(progresses[i])
        speedQueue.append(speeds[i])
    while queue:
        if queue[0] + (days * speedQueue[0]) >= 100:
            queue.popleft()
            speedQueue.popleft()
            cnt += 1
        else:
            if cnt >= 1:
                answer.append(cnt)
                cnt = 0
            days += 1
    answer.append(cnt)
    return answer
