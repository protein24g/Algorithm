def s_chk(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return 0
    return 1
n = int(input())
ary = list(map(int, input().split()))
cnt = 0
for i in ary:
    if i != 1 and s_chk(i): cnt += 1
print(cnt)
