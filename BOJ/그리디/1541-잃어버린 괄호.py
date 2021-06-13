arr = input().split('-')
arr2 = []

for i in arr:
    arr2.append(i.split('+'))

result = sum(map(int, arr2[0]))

for i in range(1, len(arr2)):
    result -= sum(map(int, arr2[i]))

print(result)
