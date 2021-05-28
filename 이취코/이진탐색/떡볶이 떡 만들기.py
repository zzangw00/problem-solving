def binarySearch(arr, target, start, end):
    while start <= end:
        result = 0
        mid = (start + end) // 2
        for i in arr:
            if i > mid:
                result += i - mid
        if result == target:
            return mid
        if result < target:
            end = mid - 1
        else:
            start = start + 1
    return None

inputData = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binarySearch(arr, inputData[1], 0, max(arr) - 1)

print(result)