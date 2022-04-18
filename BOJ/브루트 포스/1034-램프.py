n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
k = int(input())
answer = 0


def solution():
    global answer
    for i in range(n):
        cnt = graph[i].count(0)
        cnt2 = 0
        if cnt <= k and ((cnt % 2) == (k % 2)):
            for j in range(n):
                if graph[i] == graph[j]:
                    cnt2 += 1
        answer = max(answer, cnt2)
    return answer


print(solution())
