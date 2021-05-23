score = list(map(int, input()))
first = 0
second = 0
for i in range(len(score) // 2):
    first += score[i]

for i in range(len(score) // 2, len(score)):
    second += score[i]

if first == second:
    print('LUCKY')
else:
    print('READY')