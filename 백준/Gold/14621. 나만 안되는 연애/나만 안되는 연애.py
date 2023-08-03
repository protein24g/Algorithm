def union_parent(x, y):
    x = get_parent(x)
    y = get_parent(y)

    if x < y:
        union[y] = x
    else:
        union[x] = y

def get_parent(x):
    if union[x] == x:
        return x
    else:
        x = get_parent(union[x])
        return x

def find_parent(x, y):
    x = get_parent(x)
    y = get_parent(y)

    if x == y:
        return 1
    else:
        return 0

N, M = list(map(int, input().split()))
MW = list(map(str, input().split()))

ary = []
for i in range(M):
   u, v, d = list(map(int, input().split()))
   ary.append([d, u, v])
ary.sort()

union = [0 for _ in range(N+1)]
for i in range(1, N+1):
    union[i] = i

s = 0
c = 0
for i in range(M):
    d, u, v = ary[i]
    if find_parent(u, v) == 0 and MW[u-1] != MW[v-1]:
        union_parent(u, v)
        s += d
        c += 1
if c == N-1:
    print(s)
else:
    print(-1)