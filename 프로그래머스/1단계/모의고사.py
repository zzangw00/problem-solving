def solution(answers):
    result = []
    check = []
    arr = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
           [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(3):
        count = 0
        k = 0
        for j in range(len(answers)):
            if k > len(arr[i]) - 1:
                k = 0
            if answers[j] == arr[i][k]:
                count += 1
            k += 1
        check.append(count)
    for i in range(len(check)):
        if check[i] == max(check):
            result.append(i + 1)

    return result
