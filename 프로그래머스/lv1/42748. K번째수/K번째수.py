def solution(array, commands):
    answer = []
    print(array, commands)
    for [a, b, c] in commands:
        tmp = array[a-1:b]
        tmp.sort()
        answer.append(tmp[c-1])
    return answer