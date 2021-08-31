def solution(str1, str2):
    answer = 0
    arr1 = []
    arr2 = []
    for i in range(len(str1) - 1):
        a = str1[i:i + 2]
        if a.isalpha() == True:
            arr1.append(a.lower())
    for i in range(len(str2) - 1):
        a = str2[i:i + 2]
        if a.isalpha() == True:
            arr2.append(a.lower())
    set1 = set(arr1)
    set2 = set(arr2)
    gyo = set1 & set2
    hap = set1 | set2
    a = sum([min(arr1.count(i), arr2.count(i)) for i in gyo])
    b = sum([max(arr1.count(i), arr2.count(i)) for i in hap])
    if a == 0 and b == 0:
        answer = 1
    else:
        answer = a / b

    return int(answer * 65536)
