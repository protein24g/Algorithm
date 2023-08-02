import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(cnt, n):
    global a, b, res
    if b < n: return -1
    elif b == n:
        res = min(cnt, res)
        return 1
    else:
        dfs(cnt+1, n*2)
        dfs(cnt+1, int(str(n)+'1'))
        
a, b = map(int, input().split())
res = 1e9
dfs(1, a)
if res == 1e9: print(-1)
else: print(res)
