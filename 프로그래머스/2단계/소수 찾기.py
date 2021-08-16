import math
from itertools import permutations


def isPrimeNumber(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def solution(numbers):
    answer = []
    temp = []
    arr = []
    array = []
    for i in range(1, len(numbers) + 1):
        temp.append(list(permutations(numbers, i)))
    for i in range(len(temp)):
        for j in temp[i]:
            arr.append(j)
    result = list(set([tuple(i) for i in arr]))
    for i in range(len(result)):
        array.append(int(''.join(result[i])))
    for i in array:
        if isPrimeNumber(i):
            answer.append(i)
    answer = set(answer)
    return len(answer)
