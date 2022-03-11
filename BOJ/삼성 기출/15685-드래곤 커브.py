n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def solution(arr):
    answer = 0
    visited = [[0] * 101 for _ in range(101)]
    dx = [1, 0, -1, 0]  # 0, 1, 2, 3
    dy = [0, -1, 0, 1]
    curve = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        x, y, d, g = arr[i]
        curve[i].append(d)
        for _ in range(g):
            reverse = list(reversed(curve[i]))
            for j in reverse:
                if j + 1 == 4:
                    curve[i].append(0)
                else:
                    curve[i].append(j + 1)
    for i in range(len(arr)):
        x, y, d, g = arr[i]
        visited[y][x] = 1
        for j in curve[i]:
            x = x + dx[j]
            y = y + dy[j]
            if 0 <= x <= 100 and 0 <= y <= 100:
                visited[y][x] = 1
    for x in range(100):
        for y in range(100):
            if visited[x][y] == 1 and visited[x + 1][y] == 1 and visited[x + 1][y + 1] == 1 and visited[x][y + 1] == 1:
                answer += 1

    return answer


print(solution(arr))
