def solution(a, b):
    answer = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    days = 0
    for i in range(1, a):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            days += 31
        elif i == 2:
            days += 29
        else:
            days += 30
    days += (b - 1)
    day = days % 7
    day = 5 + day - 7
    return answer[day]
