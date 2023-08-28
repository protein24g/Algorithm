import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ary = []

for _ in range(n):
    ary.append(list(map(str, input())))

t1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'] 
t2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
res = 1e9
for i in range(n-7):
    for j in range(m-7):
        d1, d2 = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if k % 2 == 0:
                    if ary[k][l] != t1[j-l]:
                        d1 += 1
                    if ary[k][l] != t2[j-l]:
                        d2 += 1
                elif k % 2 == 1:
                    if ary[k][l] != t2[j-l]:
                        d1 += 1
                    if ary[k][l] != t1[j-l]:
                        d2 += 1
        res = min(res, d1, d2)
print(res)
                    
