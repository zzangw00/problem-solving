import math

n = int(input())
people = list(map(int, input().split()))
b, c = map(int, input().split())


def solution():
    answer = 0
    for i in range(len(people)):
        people[i] -= b
        answer += 1
        if people[i] > 0:
            answer += math.ceil(people[i] / c)
    return answer


print(solution())
