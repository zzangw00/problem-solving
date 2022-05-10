temp = []
arr = []


def solution(relation):
    for i in range(1, len(relation[0]) + 1):
        dfs(i, 0, len(relation[0]), relation)
    return len(arr)


def dfs(cnt, a, count, relation):
    if len(temp) == cnt:
        check(temp, relation)
        return
    for i in range(a, count):
        temp.append(i)
        dfs(cnt, i + 1, count, relation)
        temp.pop()


def check(temp, relation):
    global arr
    flag = 0
    temp2 = []
    for i in range(len(relation)):
        temp3 = []
        for j in range(len(temp)):
            temp3.append(relation[i][temp[j]])
        temp2.append(tuple(temp3))

    if len(temp2) == len(set(temp2)):
        if not arr:
            arr.append(''.join(map(str, temp)))
        else:
            for i in arr:
                cnt = 0
                for j in i:
                    if j in ''.join(map(str, temp)):
                        cnt += 1
                if cnt == len(i):
                    flag = 1
                    break
            if flag == 0:
                arr.append(''.join(map(str, temp)))
