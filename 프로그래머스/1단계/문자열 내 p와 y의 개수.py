def solution(s):
    arr = list(s)
    pCount = 0
    yCount = 0
    for i in arr:
        if i == 'P' or i == 'p':
            pCount += 1
        if i == 'Y' or i == 'y':
            yCount += 1
    if pCount == 0 and yCount == 0:
        answer = True
    else:
        if pCount == yCount:
            answer = True
        if pCount != yCount:
            answer = False

    return answer
