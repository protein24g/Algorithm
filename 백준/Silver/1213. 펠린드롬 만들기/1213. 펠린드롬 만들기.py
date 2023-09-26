s = list(map(str, input()))
s.sort()
d = {}
for  i in s: d[i] = d.get(i, 0) + 1

odd_cnt = 0
odd_txt = ''

res = ''
for i in d:
    if d[i] % 2 != 0:
        odd_cnt += 1
        odd_txt += i
        if odd_cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()

for i in d:
    for j in range(d[i] // 2):
        res += i
        
print(res + odd_txt + res[::-1])
