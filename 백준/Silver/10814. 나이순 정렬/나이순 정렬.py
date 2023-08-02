import sys
input = sys.stdin.readline

N = int(input())
ary = []
for i in range(N):
    a, b = list(map(str, input().split()))
    ary.append([int(a), b, int(i)])
ary.sort(key = lambda x : (x[0], x[2]))
for i in range(N):
    print(ary[i][0], ary[i][1])
