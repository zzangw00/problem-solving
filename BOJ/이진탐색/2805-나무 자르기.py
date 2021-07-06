n, m = map(int, input().split())
arr = list(map(int, input().split()))


def binarySearch(arr, target, start, end):
    answer = []
    while start <= end:
        result = 0
        mid = (start + end) // 2
        for i in arr:
            if i > mid:
                result += i - mid
        if result >= target:
            start = mid + 1
            answer.append(mid)
        else:
            end = mid - 1
    return max(answer)


print(binarySearch(arr, m, 0, max(arr)))
