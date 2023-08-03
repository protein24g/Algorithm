def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i, j in enumerate(progresses):
            progresses[i] = j + speeds[i]
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0); speeds.pop(0)
        if cnt > 0: answer.append(cnt)
        
    return answer