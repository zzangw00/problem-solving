from collections import deque
queue = deque()
answer = []
result = []
temp = []
cnt = 0
n = int(input())
for i in range(n):
    queue.append(int(input()))

for i in range(1, n + 1):
    temp.append(i)
    answer.append('+')
    while True:
        if temp[-1] == queue[0]:
            queue.popleft()
            temp.pop()
            answer.append('-')
            if not temp:
                break
        else:
            break

if temp:
    print('NO')
else:
    for i in answer:
        print(i)
