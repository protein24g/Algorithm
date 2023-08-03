def per(k):
    if k == M:
        print(*result)
        return
    for i in range(len(ary)):
        if visited[i] == 0:
            result[k] = ary[i]
            visited[i] = 1
            per(k+1)
            visited[i] = 0

N, M = list(map(int, input().split()))

ary = []
for i in range(1, N+1):
    ary.append(i)

visited = [0] * N
result = [0] * M

per(0)