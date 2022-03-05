def f(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


t = int(input())
for i in range(t):
    n, m = map(int, input().split(' '))
    print(f(m) // (f(n) * f(m - n)))
