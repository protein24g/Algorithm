n = int(input())
stack = []

for _ in range(n):
    su = int(input())
    if su == 0: stack.pop()
    else: stack.append(su)
print(sum(stack))