n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))
arr.sort()
arr.sort(key=lambda x: (len(x), sum(int(a) for a in x if a.isnumeric())))

for i in arr:
    for j in i:
        print(j, end='')
    print('')
