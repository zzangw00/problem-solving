k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))


def binarySearch(arr, target, start, end):
    answer = []
    while start <= end:
        count = 0
        mid = (start + end) // 2
        for i in arr:
            count += i // mid
        if count >= target:
            answer.append(mid)
            start = mid + 1
        else:
            end = mid - 1
    return answer


print(max(binarySearch(arr, n, 1, max(arr))))
