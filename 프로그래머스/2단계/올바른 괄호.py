def solution(s):
    answer = True
    stack = []
    arr = list(s)
    if arr[0] == ')':
        return False
    else:
        for i in range(len(arr)):
            stack.append(arr[i])
            if len(stack) > 1:
                if stack[-1] == ')':
                    if stack[-2] == '(':
                        stack.pop()
                        stack.pop()
    if stack:
        answer = False
    else:
        answer = True
    return answer
