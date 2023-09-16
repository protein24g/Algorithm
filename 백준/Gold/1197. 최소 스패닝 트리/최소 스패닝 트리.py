import sys
input = sys.stdin.readline

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

v, e = map(int, input().split())
root = [i for i in range(v+1)]
ary = []
for i in range(e):
    ary.append(list(map(int, input().split())))
ary.sort(key = lambda x : x[2])


ans = 0
for s, e, w in ary:
    sroot = find(s)
    eroot = find(e)
    if sroot != eroot:
        if sroot > eroot:
            root[sroot] = eroot
        else:
            root[eroot] = sroot
        ans += w
print(ans)
