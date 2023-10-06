import sys
input = sys.stdin.readline

N = int(input())
ary, dic = [], {}

for i in range(N):
    ary.append(list(map(str, input().strip())))
    for j,k in enumerate(ary[i]):
        dic[k] = dic.get(k, 0) + 10**(len(ary[i])-1-j)
dic = sorted(dic.items(), key = lambda x : (-x[1]))

res = 0
num = 9
for i in range(len(dic)):
    res += dic[i][1] * num
    num -= 1
print(res)
