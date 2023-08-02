n = int(input())
chk = 0
for i in range(1, n+1):
    tmp = i
    for j in str(i):
        i += int(j)
    if i == n: chk = 1; break;
    
if chk: print(tmp)
else: print(0)
