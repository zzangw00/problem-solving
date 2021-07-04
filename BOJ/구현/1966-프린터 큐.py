from collections import deque
k = int(input())
result = []
for i in range(k):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque()
    queue2 = deque()
    for j in range(n):
        queue.append((arr[j], j))
    for j in range(n):
        queue2.append(arr[j])
    count = 0
    while queue:
        if queue2[0] is not max(queue2):
            a, idx = queue.popleft()
            b = queue2.popleft()
            queue.append((a, idx))
            queue2.append(b)
        else:
            a, idx = queue.popleft()
            b = queue2.popleft()
            count += 1
            if idx == m:
                result.append(count)

for i in range(k):
    print(result[i])
