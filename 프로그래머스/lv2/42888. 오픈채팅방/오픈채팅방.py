def solution(record):
    dic = {}
    for i in range(len(record)):
        tmp = record[i].split()
        if len(tmp) == 3:dic[tmp[1]] = tmp[2]
    
    res = []
    for i in record:
        tmp = i.split()
        if tmp[0] == 'Enter': res.append('%s님이 들어왔습니다.'%(dic[tmp[1]]))
        elif tmp[0] == 'Leave': res.append('%s님이 나갔습니다.'%(dic[tmp[1]]))
    
    return res