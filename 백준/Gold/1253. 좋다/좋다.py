import sys
input = sys.stdin.readline
def find(ary, target):
    global res
    left, right = 0, len(ary) - 1
    while left < right:
        s = ary[left] + ary[right]
        if s == target:
            res += 1
            return
        elif s < target: left += 1
        else: right -= 1
        

n = int(input())
ary = sorted(map(int, input().split()))
res = 0
for i in range(n):
    find(ary[:i] + ary[i+1:], ary[i])
print(res)
