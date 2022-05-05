def solution(stones, k):
    answer = 0
    start = 1
    end = max(stones)
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0
        if cnt >= k:
            end = mid - 1
        else:
            start = mid + 1
    return start
