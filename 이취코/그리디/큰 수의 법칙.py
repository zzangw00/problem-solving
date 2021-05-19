n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
count = 0
sum = 0
while True:
    for i in range(k):
        count += 1
        if count == m + 1:
            break
        else:
            sum += arr[0]

    if count == m + 1:
        print(sum)
        break
    else:
        count += 1
        sum += arr[1]


