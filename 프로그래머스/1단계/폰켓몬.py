def solution(nums):
    answer = 0
    result = len(set(nums))
    if result >= len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = result
    return answer
