import math
def solution(fees, records):
    time_dic = dict()  # { '차량번호' : [시간,시간], '차량번호' : [시간, 시간, 시간, ...] }
    pay_dic = dict()   # { '차량번호' : 요금 }
    answer_lst = []

    for inform_text in records:
        car_num = inform_text[6:10]
        h = int(inform_text[0:2])
        m = int(inform_text[3:5])
        
        if car_num in time_dic:              # 차량 번호가 딕셔너리에 있으면
            time_dic[car_num] += [h*60 + m]
        else:                                # 차량 번호가 딕셔너리에 없으면
            time_dic[car_num] = [h*60 + m]
            pay_dic[car_num] = 0             # pay_dic정의도 동시에 해주기
    print(f'time_dic : {time_dic}')
    print(f'pay_dic : {pay_dic}')

    for car_num in time_dic:

        if len(time_dic[car_num]) % 2 != 0:     # 차량 번호 시간이 홀수개 이면
            time_dic[car_num].append(23*60 + 59)   # 마지막 out이 없는 것. 23시 59분 추가해줌
        print(f'time_dic_2 : {time_dic}')

        for i in range(len(time_dic[car_num])//2):
            in_time = time_dic[car_num][i*2]
            out_time = time_dic[car_num][i*2+1]
            pay_dic[car_num] += out_time - in_time
        print(f'pay : {pay_dic}')
    for car in sorted(pay_dic):
        print(f'car : {car}')
        basic_time = fees[0]

        if pay_dic[car] <= basic_time:   # 기본 시간 이하 기본요금
            answer_lst.append(fees[1])
        else:
            answer_lst.append(fees[1] + int(math.ceil((pay_dic[car] - basic_time)/fees[2])*fees[3]))
        print(f'answer_lst_3 : {answer_lst}')
    print(f'pay_dic_2 : {pay_dic}')

            
    return answer_lst

fee = [180, 5000, 10, 600]
rec = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fee, rec))
