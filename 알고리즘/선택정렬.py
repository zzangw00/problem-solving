arr = [4, 3, 1, 5]

for i in range(len(arr) - 1):
    Idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[Idx]:
            Idx = j
    arr[i], arr[Idx] = arr[Idx], arr[i]

print(arr)
