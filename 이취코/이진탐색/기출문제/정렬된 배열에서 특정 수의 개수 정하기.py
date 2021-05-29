n, x = map(int, input().split())
arr = list(map(int, input().split()))
none = -1


def first(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
            return mid
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


def last(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == n - 1 or target < arr[mid + 1]) and arr[mid] == target:
            return mid
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


a = first(arr, x, 0, n - 1)
b = last(arr, x, 0, n - 1)

if first(arr, x, 0, n - 1) != -1:
    print(b - a + 1)
else:
    print(none)
