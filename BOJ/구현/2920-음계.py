arr = list(map(int, input().split()))
count = 0
count2 = 0
for i in range(len(arr)):
    if arr[i] == i + 1:
        count += 1
    if arr[i] == 8 - i:
        count2 += 1

if count == 8:
    print('ascending')
elif count2 == 8:
    print('descending')
else:
    print('mixed')
