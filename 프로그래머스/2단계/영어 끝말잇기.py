def solution(n, words):
    answer = []
    stack = [words[0]]
    cnt = 2
    cnt2 = 1
    for i in range(1, len(words)):
        if words[i][0] == stack[-1][-1] and words[i] not in stack:
            stack.append(words[i])
            cnt += 1
            if cnt > n:
                cnt = 1
                cnt2 += 1
        else:
            answer.append(cnt)
            answer.append(cnt2)
            break
    if len(stack) == len(words):
        answer.append(0)
        answer.append(0)
    return answer
