def chk(k):
    global N
    while N % k == 0:
        print(k)
        N //= k


N = int(input())

ary = []

for i in range(2, N+1):
    chk(i)