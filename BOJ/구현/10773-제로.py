k = int(input())
arr = []
stack = []
for i in range(k):
    arr.append(int(input()))
for i in arr:
    if i != 0:
        stack.append(i)
    else:
        stack.pop()
print(sum(stack))
