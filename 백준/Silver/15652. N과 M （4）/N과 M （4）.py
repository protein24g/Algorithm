import sys
sys.setrecursionlimit(10**6)

def recur(dep):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    for i in range(dep, n+1):
        res.append(i)
        recur(i)
        res.pop()

n, m = map(int, input().split())
res = []
recur(1)
