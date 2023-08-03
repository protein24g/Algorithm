N, K = list(map(int, input().split()))

ary = [list(map(int, input().split())) for _ in range(N)]
ary.sort(key = lambda x:(-x[1], -x[2], -x[3]))

for i in range(N):
    if ary[i][0] == K:
        nation = i

for i in range(N):
    if ary[nation][1:] == ary[i][1:]:
        print(i+1)
        break