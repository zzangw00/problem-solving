k = []
arr = []


def solution(user_id, banned_id):
    answer = 0
    temp = []
    for i in range(len(banned_id)):
        temp2 = []
        a = banned_id[i]
        for j in range(len(user_id)):
            value = check(a, user_id[j])
            if value != -1:
                temp2.append(value)
        temp.append(temp2)
    dic = {}
    for i in range(len(user_id)):
        dic[user_id[i]] = 0
    dfs(0, dic, temp, len(banned_id))
    arr2 = []
    for i in range(len(arr)):
        arr2.append(sorted(list(arr[i].split())))
    dic2 = {}
    for i in range(len(arr2)):
        dic2[tuple(arr2[i])] = 1
    answer = len(dic2)
    return answer


def check(a, b):
    if len(a) != len(b):
        return -1
    for i in range(len(a)):
        if a[i] != '*':
            if a[i] != b[i]:
                return -1
    return b


def dfs(a, dic, temp, num):
    global arr
    if len(k) == num:
        arr.append(' '.join(k))
        return
    for i in range(a, len(temp)):
        for j in range(len(temp[i])):
            if dic[temp[i][j]] == 0:
                k.append(temp[i][j])
                dic[temp[i][j]] = 1
                dfs(i + 1, dic, temp, num)
                dic[temp[i][j]] = 0
                k.pop()
