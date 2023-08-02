n = int(input())
ary = list(map(int, input().split()))
ans = [0] * n
s = []
for i in range(n):
    while s:
        if s[-1][1] < ary[i]:
            s.pop()
        else:            
            ans[i] = s[-1][0] + 1
            break
    s.append([i, ary[i]])
print(*ans)