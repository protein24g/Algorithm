n = int(input())
ary, stack = [], []

for _ in range(n):
    ary.append(list(map(str, input().split())))
for i in range(n):
    if ary[i][0] == 'push':
        stack.append(int(ary[i][1]))
    elif ary[i][0] == 'top':
        if len(stack) == 0: print('-1')
        else: print(stack[-1])
    elif ary[i][0] == 'size':
        print(len(stack))
    elif ary[i][0] == 'empty':
        if len(stack) == 0: print('1')
        else: print('0')
    elif ary[i][0] == 'pop':
        if len(stack) == 0: print('-1')
        else: print(stack.pop())
