import sys
input = sys.stdin.readline

ary = []
N = int(input())
for i in range(N):
    ary.append(int(input()))

ary.sort()
for i in range(len(ary)):
    print(ary[i])