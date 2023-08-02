def s_chk(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return 0
    return 1
m, n = map(int, input().split())
for i in range(m, n+1):
    if i == 1: continue
    if s_chk(i): print(i)
