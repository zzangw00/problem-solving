arr = list(input())
result = []
sum = 0
for i in arr:
    if ord(i) >= 65:
        result.append(i)
    else:
        sum += int(i)
result.sort()
result.append(sum)

for i in result:
    print(i, end='')