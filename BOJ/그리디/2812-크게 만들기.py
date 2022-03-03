n, k = map(int, input().split())
arr = list(map(int, input()))


def solution(arr, k):
    stack = []
    for i in range(len(arr)):
        while k > 0 and stack:
            if arr[i] > stack[-1]:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(arr[i])
    if k != 0:
        for i in range(k):
            stack.pop()
    return stack


a = solution(arr, k)
print(''.join(map(str, a)))
