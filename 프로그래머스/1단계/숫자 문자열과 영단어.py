def solution(s):
    answer = []
    arr = list(s)
    result = []
    number = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i in range(len(arr)):
        if arr[i] in number:
            answer.append(arr[i])
        else:
            result.append(arr[i])
            a = ''.join(result)
            if a in dict:
                answer.append(dict[a])
                result = []

    realAnswer = ''.join(answer)
    return int(realAnswer)
