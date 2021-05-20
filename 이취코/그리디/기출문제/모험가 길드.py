n = int(input())
arr = list(map(int, input().split()))
count = 0
group = 0
arr.sort()

for i in arr:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)