from collections import deque
import copy

t = int(input())
temp = deque([])
arr = ['+', '-', ' ']


def solution(n):
    answer = []
    dfs(n, answer)
    return answer


def dfs(n, answer):
    if len(temp) == n - 1:
        check(temp, answer, n)
        return
    for i in range(3):
        temp.append(arr[i])
        dfs(n, answer)
        temp.pop()


def check(temp, answer, n):
    temp2 = copy.deepcopy(temp)
    arr2 = []
    stack = []
    for i in range(1, n + 1):
        arr2.append(str(i))
        if temp2:
            arr2.append(temp2.popleft())
    for i in range(len(arr2)):
        if arr2[i] != ' ':
            stack.append(arr2[i])
    stack2 = [stack[0]]
    for i in range(1, len(stack)):
        if stack2[-1].isdigit() == True and stack[i].isdigit() == True:
            a = stack2.pop()
            b = a + stack[i]
            stack2.append(b)
        else:
            stack2.append(stack[i])
    result = int(stack2[0])
    if len(stack2) > 1:
        for i in range(1, len(stack2) - 1):
            if stack2[i] == '+':
                result += int(stack2[i + 1])
            elif stack2[i] == '-':
                result -= int(stack2[i + 1])
    if result == 0:
        answer.append(arr2)


k = []
for _ in range(t):
    k.append(int(input()))
for i in range(len(k)):
    aa = solution(k[i])
    aa.sort()
    for j in aa:
        print(''.join(map(str, j)))
    if i < len(k) - 1:
        print()
