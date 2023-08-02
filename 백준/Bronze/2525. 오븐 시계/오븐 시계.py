h, m = map(int, input().split())
c = int(input())
tmp = m + c
if tmp // 60 > 0:
    h += tmp // 60
    if h >= 24:
        h -= 24
    m = tmp % 60
else:
    m = tmp
print(h, m)
    
