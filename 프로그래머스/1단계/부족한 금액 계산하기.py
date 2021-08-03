def solution(price, money, count):
    answer = 0
    total = 0
    prices = 0
    for _ in range(count):
        prices += price
        total += prices

    if total > money:
        answer = total - money
    else:
        answer = 0

    return answer
