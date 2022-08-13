def solution(record):
    answer = []
    name_dic = dict()
    for name in record:
        information = list(name.split())
        if information[0] == 'Enter' or information[0] == 'Change':
            name_dic[information[1]] = information[2]
    for status in record:
        enter_leave = list(status.split())
        if enter_leave[0] == 'Enter':
            answer.append(name_dic[enter_leave[1]] + '님이 들어왔습니다.')
        elif enter_leave[0] == 'Leave':
            answer.append(name_dic[enter_leave[1]] + '님이 나갔습니다.')
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))