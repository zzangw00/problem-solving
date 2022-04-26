from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
graph = deque([])
people = deque([])
for i in range(len(arr)):
    graph.append(arr[i])
    people.append(0)


def solution():
    answer = 0
    while True:
        answer += 1
        a = graph.pop()
        graph.appendleft(a)
        a = people.pop()
        people.appendleft(a)
        if people[n - 1] == 1:
            people[n - 1] = 0
        for i in range(n - 2, -1, -1):
            if people[i] == 1 and people[i + 1] == 0 and graph[i + 1] > 0:
                people[i] = 0
                people[i + 1] = 1
                graph[i + 1] -= 1
        if people[n - 1] == 1:
            people[n - 1] = 0
        if graph[0] > 0 and people[0] == 0:
            graph[0] -= 1
            people[0] = 1
        if graph.count(0) >= k:
            break

    return answer


print(solution())
