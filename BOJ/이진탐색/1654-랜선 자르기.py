k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))


def binarySearch(arr, target, start, end):
    answer = []
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for i in arr:
            cnt += i // mid
        if cnt >= target:
            answer.append(mid)
            start = mid + 1
        else:
            end = mid - 1
    return answer


print(max(binarySearch(arr, n, 1, max(arr))))
