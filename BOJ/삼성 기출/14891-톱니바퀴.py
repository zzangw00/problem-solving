from collections import deque

arr = []
for _ in range(4):
    arr.append(deque(list(map(int, input()))))
k = int(input())
spins = []
for _ in range(k):
    spins.append(list(map(int, input().split(' '))))


def solution(arr, spins):
    queue = deque([])
    answer = 0
    for i in range(len(spins)):
        visited = [0, 0, 0, 0]
        a = spins[i][0] - 1
        if a % 2 == 1:
            v = [1, spins[i][1]]
        else:
            v = [0, spins[i][1]]
        queue.append(spins[i][0] - 1)
        while queue:
            x = queue.popleft()
            right = x + 1
            left = x - 1
            if right <= 3 and visited[right] == 0:
                if arr[x][2] != arr[right][6]:
                    queue.append(right)
            if left >= 0 and visited[left] == 0:
                if arr[x][6] != arr[left][2]:
                    queue.append(left)
            if v[0] == x % 2:
                spin(arr[x], v[1])
                visited[x] = 1
            else:
                if v[1] == 1:
                    spin(arr[x], -1)
                    visited[x] = 1
                else:
                    spin(arr[x], 1)
                    visited[x] = 1
    for i in range(4):
        if arr[i][0] == 1:
            answer += 2 ** i
    return answer


def spin(arr, v):
    if v == 1:
        a = arr.pop()
        arr.appendleft(a)
    else:
        a = arr.popleft()
        arr.append(a)


print(solution(arr, spins))
