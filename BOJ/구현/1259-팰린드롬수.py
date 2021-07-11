answer = []
while True:
    arr = list(input())
    count = 0
    if arr == ['0']:
        break
    if len(arr) == 1:
        answer.append('yes')
    for i in range(len(arr) // 2):
        if arr[i] == arr[len(arr) - 1 - i]:
            count += 1
            if count == len(arr) // 2:
                answer.append('yes')
        if arr[i] != arr[len(arr) - 1 - i]:
            answer.append('no')
            break

for i in answer:
    print(i)
