answer = []
temp = ['[', ']', '(', ')']
while True:
    stack = []
    stack2 = []
    arr = input()
    if len(arr) == 1:
        break
    for i in range(len(arr)):
        if arr[i] in temp:
            stack.append(arr[i])
    for i in range(len(stack)):
        stack2.append(stack[i])
        if len(stack2) >= 2:
            if stack2[-1] == ']':
                if stack2[-2] == '[':
                    stack2.pop()
                    stack2.pop()
            elif stack2[-1] == ')':
                if stack2[-2] == '(':
                    stack2.pop()
                    stack2.pop()
    if stack2:
        answer.append('no')
    else:
        answer.append('yes')
print(answer)
