def solution(answers):
    answer = []
    one_res = [1, 2, 3, 4, 5]
    two_res = [2, 1, 2, 3, 2, 4, 2, 5]
    thr_res = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one_chk = 0; two_chk = 0; thr_chk = 0
    one_cur = 0; two_cur = 0; thr_cur = 0
    for i in range(len(answers)):
        one_cur = i % 5
        two_cur = i % 8
        thr_cur = i % 10
        
        if answers[i] == one_res[one_cur]:
            one_chk += 1
        if answers[i] == two_res[two_cur]:
            two_chk += 1
        if answers[i] == thr_res[thr_cur]:
            thr_chk += 1
    
    m = max(one_chk, two_chk, thr_chk)
    if m == one_chk:
        answer.append(1)
    if m == two_chk:
        answer.append(2)
    if m == thr_chk:
        answer.append(3)
            
    return answer