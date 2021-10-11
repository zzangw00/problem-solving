a = list(map(int, input().split()))
result = []


def solution(a, start, end):
    sum = 0
    for i in range(start, end):
        sum += a[i]
    result.append(sum)
    print(result)
    end = end - 1
    if start == end:
        return
    return solution(a, start, end)


solution(a, 0, len(a))

# print(max(result))
