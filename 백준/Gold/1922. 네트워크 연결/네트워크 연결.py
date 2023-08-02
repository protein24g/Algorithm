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
        union[x] = get_parent(union[x])
        return union[x]

def find_parent(x, y):
    x = get_parent(x)
    y = get_parent(y)

    if x == y:
        return 1
    else:
        return 0

N = int(input())
M = int(input())

union = [0] * (N+1)
for i in range(1, N+1):
    union[i] = i

cost_ary = []

for i in range(M):
    x, y, c = list(map(int, input().split()))
    cost_ary.append((c, x, y))

cost_ary.sort()

result = 0
for i in range(len(cost_ary)):
    c, x, y = cost_ary[i]
    if find_parent(x, y) == 0:
        union_parent(x, y)
        result += c
print(result)
