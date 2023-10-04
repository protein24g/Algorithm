import sys
input = sys.stdin.readline

n = int(input())
ary = []
for _ in range(n):
    ary.append(list(map(int, input().split())))
ary.sort(key = lambda x : (x[1], x[0]))

end, cnt = 0, 0
for i in range(n):
    if ary[i][0] >= end:
        end = ary[i][1]
        cnt += 1
print(cnt) 
