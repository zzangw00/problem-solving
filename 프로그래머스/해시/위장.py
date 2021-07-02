def solution(clothes):
    answer = 1
    arr = {}
    for i in clothes:
        key = i[1]
        value = i[0]
        if key in arr:
            arr[key] += 1
        else:
            arr[key] = 1
    for i in arr.keys():
        answer = answer * (arr[i] + 1)
    return answer - 1
