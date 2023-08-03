import sys
input = sys.stdin.readline

N = int(input())
ary = []
for i in range(N):
  ary.append(int(input()))
max = ary[-1]
cnt = 1
for i in range(len(ary)-1, -1, -1):
  if max < ary[i]:
    cnt += 1
    max = ary[i]
print(cnt)