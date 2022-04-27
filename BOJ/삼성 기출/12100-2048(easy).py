import copy

n = int(input())
graph2 = []
for _ in range(n):
    graph2.append(list(map(int, input().split())))
arr = ['U', 'D', 'L', 'R']
temp = []
answer = 0


def solution():
    dfs()
    return answer


def dfs():
    if len(temp) == 5:
        check(temp)
        return
    for i in range(4):
        temp.append(arr[i])
        dfs()
        temp.pop()


def check(temp):
    global answer
    graph = copy.deepcopy(graph2)
    for i in range(len(temp)):
        if temp[i] == 'D':
            for y in range(n):
                stack = []
                for x in range(n - 1, -1, -1):
                    if graph[x][y] != 0:
                        if not stack:
                            stack.append([graph[x][y], 0])
                        else:
                            if stack[-1][0] == graph[x][y] and stack[-1][1] == 0:
                                stack.pop()
                                stack.append([graph[x][y] * 2, 1])
                            else:
                                stack.append([graph[x][y], 0])
                for a in range(n - len(stack)):
                    stack.append([0, 0])
                for x in range(n - 1, -1, -1):
                    graph[x][y] = stack[n - 1 - x][0]
        elif temp[i] == 'U':
            for y in range(n):
                stack = []
                for x in range(n):
                    if graph[x][y] != 0:
                        if not stack:
                            stack.append([graph[x][y], 0])
                        else:
                            if stack[-1][0] == graph[x][y] and stack[-1][1] == 0:
                                stack.pop()
                                stack.append([graph[x][y] * 2, 1])
                            else:
                                stack.append([graph[x][y], 0])
                for a in range(n - len(stack)):
                    stack.append([0, 0])
                for x in range(n):
                    graph[x][y] = stack[x][0]
        elif temp[i] == 'L':
            for x in range(n):
                stack = []
                for y in range(n):
                    if graph[x][y] != 0:
                        if not stack:
                            stack.append([graph[x][y], 0])
                        else:
                            if stack[-1][0] == graph[x][y] and stack[-1][1] == 0:
                                stack.pop()
                                stack.append([graph[x][y] * 2, 1])
                            else:
                                stack.append([graph[x][y], 0])
                for a in range(n - len(stack)):
                    stack.append([0, 0])
                for y in range(n):
                    graph[x][y] = stack[y][0]
        elif temp[i] == 'R':
            for x in range(n):
                stack = []
                for y in range(n - 1, -1, -1):
                    if graph[x][y] != 0:
                        if not stack:
                            stack.append([graph[x][y], 0])
                        else:
                            if stack[-1][0] == graph[x][y] and stack[-1][1] == 0:
                                stack.pop()
                                stack.append([graph[x][y] * 2, 1])
                            else:
                                stack.append([graph[x][y], 0])
                for a in range(n - len(stack)):
                    stack.append([0, 0])
                for y in range(n - 1, -1, -1):
                    graph[x][y] = stack[n - 1 - y][0]
    for x in range(n):
        for y in range(n):
            answer = max(answer, graph[x][y])


print(solution())
