import sys
input = sys.stdin.readline

n, s = list(map(int, input().split()))
ary = list(map(int, input().split()))
left, right, res = 0, 0, 1e9
r_sum = ary[0]
while right <= len(ary):
    if r_sum < s:
        right += 1
        if right < len(ary):
            r_sum += ary[right]
    elif r_sum > s:
        res = min(res, right - left + 1)
        r_sum -= ary[left]
        left += 1
    else:
        res = min(res, right - left + 1)
        r_sum -= ary[left]
        left += 1
        
if res == 1e9: print(0)
else: print(res)
    
