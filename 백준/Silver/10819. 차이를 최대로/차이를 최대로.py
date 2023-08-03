def npr(k):
    global N, score
    if k == N:
        tmp = 0
        for i in range(1, N):
            tmp += abs(result[i-1] - result[i])
        score = max(score, tmp)
    for i in range(N):
        if visited[i] == 0:
            result.append(ary[i])
            visited[i] = 1
            npr(k+1)
            result.pop()
            visited[i] = 0

N = int(input())

ary = list(map(int, input().split()))
visited = [0] * N
result = []
score = 0
npr(0)
print(score)