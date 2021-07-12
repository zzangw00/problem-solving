n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
target = list(map(int, input().split()))

dic = dict()
answer = []
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if target[i] in dic:
        answer.append(dic[target[i]])
    else:
        answer.append(0)

for i in answer:
    print(i, end=' ')
