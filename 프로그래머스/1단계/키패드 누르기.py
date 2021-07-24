def solution(numbers, hand):
    answer = []
    leftHand = '*'
    rightHand = '#'
    left = [1, 4, 7, '*']
    right = [3, 6, 9, '#']
    center = [2, 5, 8, 0]
    for i in range(len(numbers)):
        if numbers[i] in left:
            answer.append('L')
            leftHand = numbers[i]
            continue
        if numbers[i] in right:
            answer.append('R')
            rightHand = numbers[i]
            continue
        else:
            if leftHand not in center:
                leftR = center.index(numbers[i]) - left.index(leftHand)
                if leftR < 0:
                    leftR = -leftR
                leftR += 1
            else:
                leftR = center.index(numbers[i]) - center.index(leftHand)
                if leftR < 0:
                    leftR = -leftR
            if rightHand not in center:
                rightR = center.index(numbers[i]) - right.index(rightHand)
                if rightR < 0:
                    rightR = -rightR
                rightR += 1
            else:
                rightR = center.index(numbers[i]) - center.index(rightHand)
                if rightR < 0:
                    rightR = -rightR

            if leftR > rightR:
                answer.append('R')
                rightHand = numbers[i]
                continue
            if leftR < rightR:
                answer.append('L')
                leftHand = numbers[i]
                continue
            else:
                if hand == 'right':
                    answer.append('R')
                    rightHand = numbers[i]
                    continue
                else:
                    answer.append('L')
                    leftHand = numbers[i]
                    continue
    result = ''.join(answer)
    return result
