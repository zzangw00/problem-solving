arr = [4, 3, 5, 1]

for _ in range(len(arr)):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

print(arr)
