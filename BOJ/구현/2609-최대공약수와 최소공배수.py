a, b = map(int, input().split())

answer = 0
answer2 = 0

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        answer = i
        answer2 = i * (a // i) * (b // i)

print(answer)
print(answer2)
