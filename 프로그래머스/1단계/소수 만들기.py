from itertools import combinations


def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))
    for i in range(len(arr)):
        count = 0
        result = sum(list(arr[i]))
        for j in range(2, result):
            count += 1
            if result % j == 0:
                count = 0
                break
            if count == result - 2:
                answer += 1
                count = 0
    return answer
