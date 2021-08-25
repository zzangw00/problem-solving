def solution(s):
    stack = []
    for i in s:
        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack:
        answer = 0
    else:
        answer = 1
    return answer
