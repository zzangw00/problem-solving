def solution(number, k):
    stack = [number[0]]
    for i in range(1, len(number)):
        while stack and number[i] > stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number[i])
    if k > 0:
        for i in range(k):
            stack.pop()

    return ''.join(stack)
