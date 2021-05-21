arr = list(map(int, input()))

result = arr[0]
for i in range(len(arr) - 1):
    if arr[i] == 0 or arr[i] == 1 or arr[i + 1] == 0 or arr[i + 1] == 1:
        result = result + arr[i + 1]
    else:
        result = result * arr[i + 1]

print(result)