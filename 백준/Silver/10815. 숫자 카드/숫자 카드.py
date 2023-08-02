n = int(input())
n_ary = list(map(int, input().split()))
m = int(input())
m_ary = list(map(int, input().split()))

dic = {}
for i in n_ary: dic[str(i)] = '1'
for i in m_ary:
    if str(i) in dic: print(1, end=' ')
    else: print(0, end=' ')
