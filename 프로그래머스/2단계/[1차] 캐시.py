from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        answer = 5 * len(cities)
    else:
        for i in range(len(cities)):
            if cities[i].lower() in cache:
                answer += 1
                cache.remove(cities[i].lower())
                cache.append(cities[i].lower())
            else:
                answer += 5
                if len(cache) == cacheSize:
                    cache.popleft()
                    cache.append(cities[i].lower())
                else:
                    cache.append(cities[i].lower())

    return answer
