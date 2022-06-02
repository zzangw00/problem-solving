n = int(input())
cnt = 0
while True:
    cnt += 1
    if n % 5 == 0:
        n -= 5
    elif n % 5 != 0 and n % 2 != 0:
        n -= 2
    else:
        n -= 2
    if n < 1:
        break

if n < 0:
    print(-1)
else:
    print(cnt)
