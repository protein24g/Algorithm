import sys
input = sys.stdin.readline

s = input().strip()
stack = []

cur = 0
while cur < len(s):
    if s[cur] == '<':
        if stack:
            while stack:
                print(stack.pop(),end='')
        while s[cur] != '>':
            print(s[cur],end='')
            cur += 1
        if s[cur] == '>':
            print('>',end='')
            cur += 1
    elif s[cur] != ' ':
        stack.append(s[cur])
        cur += 1
    else:
        if stack:
            while stack:
                print(stack.pop(),end='')
        print(' ',end='')
        cur += 1
if stack:
    while stack:
        print(stack.pop(),end='')
