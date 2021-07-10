n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
arr.sort()


def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for i in find:
    print(binarySearch(arr, i, 0, n - 1))
