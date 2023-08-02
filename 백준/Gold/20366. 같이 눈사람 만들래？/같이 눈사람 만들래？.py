import sys

def two_p():
    global res
    
    for i in range(n):
        for j in range(i+3, n):
            left, right = i+1, j-1
            while left < right:
                tmp = (ary[left] + ary[right]) - (ary[i] + ary[j])
                if abs(res) > abs(tmp):
                    res = abs(tmp)
                elif tmp == 0:
                    res = 0
                    return
                if tmp > 0: right -= 1
                else: left += 1
        else:
            continue
        break

input = sys.stdin.readline
n = int(input())
ary = list(map(int, input().split()))
ary.sort()
res = sys.maxsize
two_p()
print(res)
                
