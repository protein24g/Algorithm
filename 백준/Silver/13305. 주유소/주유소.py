import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
ary = list(map(int, input().split()))

start = ary[0]
res = tmp = 0
for i in range(1, len(ary)):
    tmp += length[i-1]
    if start >= ary[i]:
        res += start * tmp
        start = ary[i]
        tmp = 0
print(res)
