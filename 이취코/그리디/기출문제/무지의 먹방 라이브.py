def solution(food_times, k):
    answer = 0
    count = 0
    if sum(food_times) <= k:
        return -1
    while True:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue
            else:
                food_times[i] -= 1
                count += 1
                if count == k + 1:
                    answer = i + 1
                    break
        if count == k + 1:
            break
    return answer