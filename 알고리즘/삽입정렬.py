arr = [4, 3, 1, 5]

for end in range(1, len(arr)):
    for i in range(end, 0, -1):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]

print(arr)
