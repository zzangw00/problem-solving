def solution(dartResult):
    answer = 0
    temp = ''
    temp2 = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            temp += dartResult[i]
        if dartResult[i] == 'S':
            temp = int(temp) ** 1
            temp2.append(temp)
            temp = ''
        if dartResult[i] == 'D':
            temp = int(temp) ** 2
            temp2.append(temp)
            temp = ''
        if dartResult[i] == 'T':
            temp = int(temp) ** 3
            temp2.append(temp)
            temp = ''
        if dartResult[i] == '#':
            temp2[-1] = temp2[-1] * -1
        if dartResult[i] == '*':
            if len(temp2) > 1:
                temp2[-1] = temp2[-1] * 2
                temp2[-2] = temp2[-2] * 2
            else:
                temp2[-1] = temp2[-1] * 2

    return sum(temp2)
