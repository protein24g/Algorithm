N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for i in range(N):
    res += max(A) * min(B)
    A.pop(A.index(max(A)))
    B.pop(B.index(min(B)))
print(res)