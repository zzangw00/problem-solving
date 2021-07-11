answer = []
n = int(input())
for i in range(n):
    arr = list(input())
    stack = []
    for j in range(len(arr)):
        stack.append(arr[j])
        if stack[len(stack) - 2] == '(' and stack[len(stack) - 2] != stack[len(stack) - 1]:
            stack.pop()
            stack.pop()
    if stack:
        answer.append('NO')
    else:
        answer.append('YES')

for i in answer:
    print(i)
