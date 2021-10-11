a = list(map(int, input().split()))
result = []


def solution(a, start, end):
    sum = 0
    for i in range(start, end):
        sum += a[i]
    result.append(sum)
    end = end - 1
    if start == end:
        return
    return solution(a, start, end)


for i in range(len(a)):
    solution(a, i, len(a))
print(result)
