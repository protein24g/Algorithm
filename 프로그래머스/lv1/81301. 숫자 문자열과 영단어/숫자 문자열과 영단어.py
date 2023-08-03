def solution(s):
    answer = ''
    dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3'
          ,'four':'4', 'five':'5', 'six':'6', 'seven':'7'
          ,'eight':'8', 'nine':'9'}
    tmp = ''
    for i, j in enumerate(s):
        if j.isdigit():
            answer += j
        else:
            tmp += j
            if tmp in dic:
                answer += dic.get(tmp)
                tmp = ''
    return int(answer)