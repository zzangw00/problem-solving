def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):
        arr = ""
        temp = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if temp == s[j:j + i]:
                cnt += 1
            else:
                if cnt != 1:
                    arr = arr + str(cnt) + temp
                else:
                    arr = arr + temp
                temp = s[j:j + i]
                cnt = 1
        if cnt != 1:
            arr = arr + str(cnt) + temp
        else:
            arr = arr + temp
        answer.append(len(arr))

    return min(answer)
