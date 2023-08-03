def solution(s):
    answer = ''
    n = s.split(' ')
    for i in n:
        for j in range(len(i)):
            if j % 2 == 1: answer += i[j].lower()
            else: answer += i[j].upper()
        answer += ' '
    return answer[0:-1]