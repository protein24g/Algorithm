import sys
t = int(sys.stdin.readline())

for i in range(t):
    res = []
    n = int(sys.stdin.readline())
    for j in range(n):
        res.append(sys.stdin.readline().rstrip())
    res.sort()
    chk = 0
    for j in range(1, n):
        if res[j].startswith(res[j-1]):
            chk = 1
            break
    if chk: print("NO")
    else: print("YES")