def solution(n, arr1, arr2):
    answer = []
    graph1 = []
    graph2 = []
    result = []
    for i in arr1:
        graph1.append(list(format(i, 'b').zfill(n)))
    for i in arr2:
        graph2.append(list(format(i, 'b').zfill(n)))
    for i in range(n):
        for j in range(n):
            if graph1[i][j] == "0" and graph2[i][j] == "0":
                answer.append(' ')
            else:
                answer.append('#')
    for i in range(0, len(answer), n):
        result.append(''.join(answer[i:i+n]))
    return result
