s = input().strip()

zero, one = [], []
tmp0, tmp1 = [], []
for i in s:
    if i == '0':
        if tmp1:
            one.append([''.join(tmp1)])
        tmp1 = []
        tmp0.append('0')
    else:
        if tmp0:
            zero.append([''.join(tmp0)])
        tmp0 = []
        tmp1.append('1')
if tmp1:
    one.append([''.join(tmp1)])
elif tmp0:
    zero.append([''.join(tmp0)])
    
print(min(len(zero), len(one)))
