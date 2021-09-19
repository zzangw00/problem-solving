import re


def solution(files):
    answer = []
    files2 = []
    for i in files:
        a = re.split(r"([0-9]+)", i)
        files2.append([a, i])
    result = sorted(files2, key=lambda x: (x[0][0].lower(), int(x[0][1])))
    for i in range(len(result)):
        answer.append(result[i][1])
    return answer
