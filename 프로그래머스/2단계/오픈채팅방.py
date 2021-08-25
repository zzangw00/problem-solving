def solution(record):
    answer = []
    info = {}
    result = []
    for i in range(len(record)):
        temp = record[i].split()
        if temp[0] == 'Enter':
            answer.append([temp[1], '님이 들어왔습니다.'])
            info[temp[1]] = temp[2]
        if temp[0] == 'Leave':
            answer.append([temp[1], '님이 나갔습니다.'])
        if temp[0] == 'Change':
            info[temp[1]] = temp[2]
    for i in range(len(answer)):
        answer[i][0] = info[answer[i][0]]
    for i in answer:
        result.append(''.join(i))
    return result
