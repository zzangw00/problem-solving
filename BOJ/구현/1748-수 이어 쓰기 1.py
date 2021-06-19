n = int(input())
nCount = list(str(n))
ans = 0
if len(nCount) > 1:
    for i in range(0, len(nCount) - 1):
        ans += 9 * (10 ** i) * (i + 1)
    last = n - ((10 ** ((len(nCount)) - 1)) - 1)
    ans += last * (len(nCount))
    print(ans)
else:
    for i in range(int(nCount[0])):
        ans += 1
    print(ans)
