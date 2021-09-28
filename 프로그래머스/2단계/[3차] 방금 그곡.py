import math


def change(temp2):
    if 'A#' in temp2:
        temp2 = temp2.replace('A#', 'a')
    if 'C#' in temp2:
        temp2 = temp2.replace('C#', 'c')
    if 'D#' in temp2:
        temp2 = temp2.replace('D#', 'd')
    if 'F#' in temp2:
        temp2 = temp2.replace('F#', 'f')
    if 'G#' in temp2:
        temp2 = temp2.replace('G#', 'g')
    return temp2


def solution(m, musicinfos):
    answer = ''
    result = []
    for i in range(len(musicinfos)):
        arr = musicinfos[i].split(',')
        term1 = arr[1].split(':')
        term2 = arr[0].split(':')
        aa = (int(term1[0]) * 60) + int(term1[1])
        aaa = (int(term2[0]) * 60) + int(term2[1])
        a = aa - aaa
        temp = change(arr[3])
        m = change(m)
        b = math.ceil(a / (len(temp)))
        temp3 = (temp * b)[:a]
        temp2 = temp3[:a]
        if m in temp2:
            result.append([arr[2], a, i])
    if result:
        result2 = sorted(result, key=lambda x: (-x[1], x[2]))
        answer = result2[0][0]
    else:
        answer = "(None)"
    return answer
