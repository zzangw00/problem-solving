n = int(input())
arr = []
for i in range(n):
    arr.append(input())


def solution(arr):
    answer = 0
    temp = []
    dic = {}
    value = []
    a = 9

    for i in range(len(arr)):
        temp.append(list(arr[i]))

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] in dic:
                dic[temp[i][j]] += 10 ** ((len(temp[i]) - j - 1))
            else:
                dic[temp[i][j]] = 10 ** ((len(temp[i]) - j - 1))

    for i in dic.values():
        value.append(i)
    value.sort(reverse=True)

    for i in range(len(value)):
        answer += (value[i] * a)
        a -= 1

    return answer


print(solution(arr))
