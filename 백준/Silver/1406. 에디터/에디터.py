import sys
input = sys.stdin.readline

left = list(input().strip())
right = []

for _ in range(int(input())):
    ary = list(input().split())
    if ary[0] == 'L' and left:
        right.append(left.pop())
    elif ary[0] == 'D' and right:
        left.append(right.pop())
    elif ary[0] == 'B' and left:
        left.pop()
    elif ary[0] == 'P':
        left.append(ary[1])

ans = left + right[::-1]
print(''.join(ans))
