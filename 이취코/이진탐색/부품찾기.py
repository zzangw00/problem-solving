def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return "yes"
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return "no"

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))
result = []
for i in arr2:
    result.append(binarySearch(arr, i, 0, n - 1))

for i in result:
    print(i, end=' ')