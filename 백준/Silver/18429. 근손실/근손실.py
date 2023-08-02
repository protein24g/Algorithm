def npr(b):
    global N, K, cnt
    if b == N:
        w = 500
        for i in range(len(res)):
            w += res[i]
            w -= K
            if w < 500:
                return
        cnt += 1
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            res.append(A[i])
            npr(b+1)
            visited[i] = 0
            res.pop()
    
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
visited = [0] * N
res = []
cnt = 0
npr(0)
print(cnt)
