import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    global b
    if i < 0 or j < 0 or i >= N or j >= N:
        return False
    if visited[i][j] == 0 and ary[i][j] == b:
        visited[i][j] = 1
        for k in range(len(d)):
            x, y = d[k]
            dfs(i+x, j+y)
        return True
    return False

N = int(input())

ary = [list(map(str, input())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count1 = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if  visited[i][j] == 0:
            b = ary[i][j]
            dfs(i, j)
            count1 += 1

for i in range(N):
    for j in range(N):
        if ary[i][j] == 'R':
            ary[i][j] = 'G'

count2 = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if  visited[i][j] == 0:
            b = ary[i][j]
            dfs(i, j)
            count2 += 1

print(count1, count2)