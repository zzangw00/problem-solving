def solution(strings, n):
    answer = []
    arr = []
    for i in range(len(strings)):
        arr.append(list(strings[i]))
    arr.sort()
    arr = sorted(arr, key=lambda x: x[n])
    for i in arr:
        answer.append(''.join(i))
    return answer
