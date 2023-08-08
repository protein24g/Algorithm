import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ary = {}

for _ in range(n):
    site, pw = input().split()
    ary[site] = pw

for _ in range(m):
    print(ary[input().rstrip()])