def solution(phone_number):
    answer = []
    arr = list(phone_number)
    for i in range(len(arr) - 4):
        answer.append('*')
    for i in range(len(arr) - 4, len(arr)):
        answer.append(arr[i])
    result = ''.join(answer)
    return result
