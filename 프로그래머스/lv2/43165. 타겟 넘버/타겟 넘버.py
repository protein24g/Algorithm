def dfs(n, t, cnt, leng, res_sum):
    global res_cnt
    if cnt == leng:
        if res_sum == t:
            res_cnt += 1
        return
    
    dfs(n, t, cnt+1, leng, res_sum + n[cnt])
    dfs(n, t, cnt+1, leng, res_sum - n[cnt])
    
res_cnt = 0
def solution(numbers, target):
    global res_cnt
    
    dfs(numbers, target, 0, len(numbers), 0)
    answer = res_cnt
    return answer