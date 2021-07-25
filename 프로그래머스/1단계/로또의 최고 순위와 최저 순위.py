def solution(lottos, win_nums):
    answer = []
    low = 0
    high = 0
    for i in range(6):
        if lottos[i] in win_nums:
            low += 1
        if lottos[i] == 0:
            high += 1
    if low + high < 2:
        answer.append(6)
    else:
        answer.append(7 - (low + high))
    if low < 2:
        answer.append(6)
    else:
        answer.append(7 - low)
    return answer
