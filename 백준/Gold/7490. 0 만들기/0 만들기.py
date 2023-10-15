import sys
input = sys.stdin.readline

def dfs(depth, mz, s_len, res):
    if depth == s_len-1:
        tmp = mz + str(ary[depth])
        if eval(tmp) == 0:
            print(res+str(ary[depth]))
    elif depth <= s_len:
        dfs(depth + 1, mz + str(ary[depth]) + '', s_len, res + str(ary[depth]) + ' ')
        dfs(depth + 1, mz + str(ary[depth]) + '+', s_len, res + str(ary[depth]) + '+')
        dfs(depth + 1, mz + str(ary[depth]) + '-', s_len, res + str(ary[depth]) + '-')
        
T = int(input())

for _ in range(T):
    N = int(input())
    ary = []
    for i in range(1, N+1):
        ary.append(i)
    dfs(0, '', N, '')
    print()
