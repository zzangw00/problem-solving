from collections import deque

n, k = map(int, input().split())
belt = list(map(int, input().split()))
belt = deque(belt)


def solution(belt):
    answer = 0
    robot = deque([0] * n)
    while True:
        answer += 1
        cnt = 0
        a = belt.pop()
        belt.appendleft(a)
        robot.pop()
        robot.appendleft(0)
        if robot[-1] == 1:
            robot.pop()
            robot.append(0)
        for i in range(n - 2, -1, -1):
            if robot[i] == 1:
                if robot[i + 1] == 0 and belt[i + 1] != 0:
                    robot[i + 1] = 1
                    robot[i] = 0
                    belt[i + 1] -= 1
        if robot[-1] == 1:
            robot.pop()
            robot.append(0)
        if belt[0] != 0:
            robot[0] = 1
            belt[0] -= 1
        for i in range(len(belt)):
            if belt[i] == 0:
                cnt += 1
        if cnt >= k:
            break

    return answer


print(solution(belt))
