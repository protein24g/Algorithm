import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ary = list(map(str, input()))
cnt = 0

for i, j in enumerate(ary):
    if j == 'P':
        for a in range(i-k, i+k+1):
            if 0 <= a < n and ary[a] == 'H':
                ary[a] = 'O'
                cnt += 1
                break
print(cnt)
