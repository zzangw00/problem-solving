def solution(bridge_length, weight, truck_weights):
    answer = 0
    mid = [0] * bridge_length
    while len(mid):
        answer += 1
        mid.pop(0)
        if truck_weights:
            if sum(mid) + truck_weights[0] <= weight:
                mid.append(truck_weights.pop(0))
            else:
                mid.append(0)
    return answer
