n = input()
f_n = input()
len_n = len(n)
len_f_n = len(f_n)
res = 0
cur = 0
while cur <= len_n - len_f_n:
    chk = True
    for i in range(len_f_n):
        if n[cur+i] != f_n[i]:
            chk = False
            break
    if not chk: cur += 1
    else: cur += len_f_n; res += 1
print(res)
