from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    while queue:
        sum, idx = queue.popleft()
        idx += 1
        if idx == len(numbers):
            if sum == target:
                answer += 1
        else:
            queue.append([sum + numbers[idx], idx])
            queue.append([sum - numbers[idx], idx])
    return answer
