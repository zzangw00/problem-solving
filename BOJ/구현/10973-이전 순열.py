n = int(input())
arr = list(map(int, input().split()))


def perMu(arr):
    n = len(arr) - 1
    i = n
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1
    if i == 0:
        return False
    j = n
    while arr[i - 1] <= arr[j]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    j = n
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return True


if perMu(arr) is True:
    for i in arr:
        print(i, end=' ')
    print()
else:
    print(-1)
