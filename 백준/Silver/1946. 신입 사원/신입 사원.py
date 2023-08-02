import sys

T = int(input())

for i in range(T):
    N = int(input())
    
    ary = []
    for j in range(N):
        ary.append(list(map(int, sys.stdin.readline().split())))
    
    ary.sort()
    tmp = ary[0][1]
    count = 1

    for j in range(N):
        if tmp > ary[j][1]:
            count += 1
            tmp = ary[j][1]
    print(count)