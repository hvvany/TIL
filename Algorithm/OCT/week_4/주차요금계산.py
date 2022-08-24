import math                                 # ceil(올림) 구현 위해 math 라이브러리 가져옴

def solution(fees, records):
    time_dic = dict()                       # { '차량번호' : [시간,시간], '차량번호' : [시간, 시간, 시간, ...] }
    stay_dic = dict()                       # { '차량번호' : 누적 시간 }
    pay_lst = []                            # [14600, 34400, 5000]
    '''
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
    "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    '''
    for inform_text in records:                 # "05:34 5961 IN"  기록 정보를 하나씩 가져온다
        car_num = inform_text[6:10]             # car_num   5961
        h = int(inform_text[0:2])               # h         05
        m = int(inform_text[3:5])               # m         34      IN, OUT은 time_dic 시간 저장 리스트 길이
        
        if car_num in time_dic:                 # 차량 번호가 time_dic에 있으면
            time_dic[car_num] += [h*60 + m]     # 시:분 기록을 분으로 환산하여 리스트에 값을 추가
                                                #                 차량 번호 : [시간, 시간,...]

        else:                                   # 차량 번호가 딕셔너리에 없으면
            time_dic[car_num] = [h*60 + m]      # time_dic에      차량 번호 : [시간]    정의추가
            stay_dic[car_num] = 0               # stay_dic정의도 동시에 해주기,  초기값은 0
    # print(f'time_dic : {time_dic}')
    # print(f'stay_dic : {stay_dic}')
    for car_num in time_dic:                        # time_dic에서 차량 번호 하나씩 가져온다.

        if len(time_dic[car_num]) % 2 != 0:         # 차량 번호 값에 저장된 시간이 홀수개 이면
            time_dic[car_num].append(23*60 + 59)    # 마지막 out 기록이 없는 것. 23시 59분(1439분) 추가해줌
        # print(f'time_dic_2 : {time_dic}')

        for i in range(len(time_dic[car_num])//2):  # time_dic 시간 기록 리스트 길이(짝수)를 2로 나누어 준다
            in_time = time_dic[car_num][i*2]        # 앞의 시간은 IN 시간
            out_time = time_dic[car_num][i*2+1]     # 뒤의 시간은 OUT 시간
            stay_dic[car_num] += out_time - in_time # stay_dic 차량번호 값(초기값 0)에 머문 시간을 추가
                                                    # stay_dic      차량 번호 : OUT - IN (머문 시간)
        # print(f'stay : {stay_dic}')
    for car in sorted(stay_dic):                    # 최종 출력이 차량 번호가 작은 차량부터여서 정렬하여 가져오기
        # print(f'car : {car}')
        basic_time = fees[0]                        # 기준 시간은 fees 리스트의 0번 인덱스

        if stay_dic[car] <= basic_time:             # 기본 시간 이하는 기본요금 청구
            pay_lst.append(fees[1])                 # pay_lst에 기본 요금 추가
        else:
            pay_lst.append(fees[1] + int(math.ceil((stay_dic[car] - basic_time)/fees[2])*fees[3]))
    #     print(f'pay_lst_3 : {pay_lst}')           # 기본 시간 초과는 기본 시간, 기본 요금 빼고 계산
    # print(f'stay_dic_2 : {stay_dic}')
            
    return pay_lst                                  # pay_lst = [14600, 34400, 5000]









fee = [180, 5000, 10, 600]
rec = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT","07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fee, rec))
