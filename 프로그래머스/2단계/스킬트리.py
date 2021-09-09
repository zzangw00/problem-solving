def solution(skill, skill_trees):
    answer = 0
    arr = list(skill)
    for i in range(len(skill_trees)):
        stack = []
        cnt = 0
        for j in list(skill_trees[i]):
            if j in arr:
                stack.append(j)

        for k in range(len(stack)):
            if arr[k] == stack[k]:
                cnt += 1
            else:
                break
        if cnt == len(stack):
            answer += 1

    return answer
