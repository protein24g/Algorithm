import sys
input = sys.stdin.readline

n = int(input())
res = sum(range(1, n))
tmp = ''
s = 0
ary = input().strip()
for i in ary:
    if i.isdigit():
        tmp += i
    else:
        s += int(tmp)
        tmp = ''
s += int(tmp)
print(s - res)

