def dfs(depth, res):
    global n, add, sub, mul, div, max_res, min_res
    if depth == n:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
    else:
        if add > 0:
            add -= 1
            dfs(depth+1, res+ary[depth])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(depth+1, res-ary[depth])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(depth+1, res*ary[depth])
            mul += 1
        if div > 0:
            div -= 1
            if res >= 0:
                res //= ary[depth]
            else:
                res = (-res // ary[depth])*-1
            dfs(depth+1, res)
            div += 1
        
    
n = int(input())
ary = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_res = -1e9
min_res = 1e9
dfs(1, ary[0])
print(int(max_res))
print(int(min_res))
