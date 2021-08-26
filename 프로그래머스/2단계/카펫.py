def solution(brown, yellow):
    answer = []
    for i in range(brown):
        if 2 * (i**2) + (2 * yellow) + (2 * brown) == i * (brown + 4):
            x = i
            y = (brown + yellow) // x
    answer.append(x)
    answer.append(y)
    return answer
