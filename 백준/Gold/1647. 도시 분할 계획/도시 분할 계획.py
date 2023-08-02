import sys
input = sys.stdin.readline

def get_parent(x):
  if visited[x] == x:
    return x
  else:
    visited[x] = get_parent(visited[x])
    return visited[x]

def union(a, b):
  a = get_parent(a)
  b = get_parent(b)

  if a < b: visited[b] = a
  else: visited[a] = b

n, m = list(map(int, input().split()))
visited = [0 for _ in range(n+1)]
for i in range(1, n+1):
  visited[i] = i
ary = []
for i in range(m):
  a, b, c = list(map(int, input().split()))
  ary.append([c, a, b])
ary.sort()

select = []
s = 0
for i in range(len(ary)):
  c, a, b = ary[i]
  if get_parent(a) != get_parent(b):
    union(a, b)
    select.append(c)
    s += c
s -= select.pop()
print(s)
