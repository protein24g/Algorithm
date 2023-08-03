import itertools

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    res = []
    for i in range(len(numbers)):
        tmp = numbers[i]*5
        res.append([int(tmp[:5]), int(numbers[i])])
    res.sort(reverse=True)
    #print(res)
    for i in range(len(res)):
        answer += str(int(res[i][1]))
    
    return str(int(answer))