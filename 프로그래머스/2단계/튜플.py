def solution(s):
    answer = []
    result = []
    arr = s[2:-2]
    arr = arr.split('},{')
    arr = sorted(arr, key=len)
    for i in arr:
        a = i.split(',')
        for j in a:
            if j not in answer:
                answer.append(j)
    for i in answer:
        result.append(int(i))
    return result
