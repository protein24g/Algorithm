import sys
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))

m, c = ary[0], 0
mc = 0
for i in range(len(ary)):
    if m <= ary[i]:
        m = ary[i]
        c = 0
    else:
        c += 1
        if mc < c: mc = c
print(mc)
