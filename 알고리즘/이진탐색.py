arr = [1, 3, 4, 5, 7]

target = [7, 5]


def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in target:
    print(binarySearch(arr, i, 0, len(arr) - 1))
