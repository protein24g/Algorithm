import sys
input = sys.stdin.readline

C, L = list(map(int, input().split()))
ary = []
for i in range(C):
    ary.append(int(input()))
    
start = 1
end = max(ary)
res = 0
while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        mid = 1
    cnt = 0
    for i in range(C):
        cnt += ary[i] // mid
    if cnt >= L:
        res = max(res, mid)
        start = mid + 1
    else:
        end = mid - 1
print(sum(ary) - (L*res))
