import requests
import datetime

#날짜로 최신 회차 계산하여 최대 입력값 보이도록
day_now = datetime.date.today()
day_init = datetime.date(2022,7,16)  # 1024회 기준 날짜. 기준 날짜를 바탕으로 최신 회차 계산
day_dif = day_now - day_init         # 기준 날짜와 차이 계산

#입력값 받기
day = int(input(f'비교 회차 개수 (최대 {1024+int((day_dif.days-1)/7)}회) : '))  # 날짜 차이 7로 나눠 최신 회차가 
                                                                            # 몇 회차인지 파악하여 최대 입력값 설정
pick_lst = list(map(int,input('1~45 사이 숫자 7개 입력 : ').split()))        # 선택한 숫자는 pick_lst에 저장

#프로그램 진행률 표현을 위한 초기값 설정
per_cnt = 0        # 진행률(%) 표현을 위한 초기값
print_cnt = 0      # 진행률 퍼센트 중복 제거 계산을 위한 초기값
print('진행률(%)')  # 반복문 돌기 전 출력하여 진행률 표현 준비
pass               # pass 안하면 마지막에 다 완료하고 뜬다.

#등수 계산을 위한 초기값 설정
cnt_1, cnt_2, cnt_3, cnt_4, cnt_5 = 0, 0, 0, 0, 0   # 1등부터 5등까지 누적 당첨 횟수 초기값
result = {}                                         # {1등: 1번, 2등: 3번,...} 최종 결과물 기록장

#회차별 데이터 불러오기
for i in range(1,day+1):  # 1회차 부터 입력한 회차까지 결과를 하나씩 반복하여 불러온다
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={i}'
    response = requests.get(url).json()
    flex_lst = []         # 보너스를 제외한 메인 볼 6개 저장소
    score = 0             # 보너스 계산을 통해 2등을 갈라야 해서 점수로 등수 나눈다.

#불러온 데이터 필터링
    for text in response:                     # 불러온 response딕셔너리에서 키를 하나씩 불러온다. 
        if text[:6] == 'drwtNo':              # 메인 볼은 키가 'drwtNo1'처럼 왼쪽5글자가 일정하므로 이 특징을 통해 메인볼 6개 구별.
            flex_lst.append(response[text])   # 메인 볼은 flex_lst에 저장
        if text == 'bnusNo':                  # 보너스 볼은 왼쪽 글자가 'bnusNo'
            bonus = response[text]            # 보너스는 메인볼과 구분하여야 하므로 따로 bonus변수에 할당

#뽑은 숫자와 당첨 번호 비교
    for num in flex_lst:       # 메인볼 6개 하나씩 불러와서 비교
        if num in pick_lst:    # 뽑은 숫자와 메인볼 비교
            score += 2         # 메인볼과 같으면 score 2점 추가
    if bonus in pick_lst:      # 보너스 볼이면 score 1점만 추가
        score += 1

# 등수 계산
    if score >= 12:            # 1등이면 메인볼 6개 이므로 총 12점
        cnt_1 += 1               # 1등 당첨 횟수 누적기록
    elif score >= 11:          # 2등이면 메인볼 5개 보너스볼 1개 11점
        cnt_2 += 1               # 2등 당첨 횟수 누적기록
    elif score >= 10:          # 3등이면 메인볼 5개
        cnt_3 += 1               # 3등 당첨 횟수 누적기록
    elif score >= 8:           # 4등이면 메인볼 4개
        cnt_4 += 1               # 4등 당첨 횟수 누적기록
    elif score >= 6:           # 5등이면 메인볼 3개
        cnt_5 += 1               # 5등 당첨 횟수 누적기록

# result 딕셔너리에 누적 당첨 횟수 기록
    result['1등 당첨 횟수']=cnt_1
    result['2등 당첨 횟수']=cnt_2
    result['3등 당첨 횟수']=cnt_3
    result['4등 당첨 횟수']=cnt_4
    result['5등 당첨 횟수']=cnt_5

# 진행률 표시를 위한 구문 => 시간이 생각보다 오래 걸려서 제대로 작동중인지 확인 필요   
    if i/day == 1:                      
        print("100% 완료!!")
    elif i/day >= 0.9 and per_cnt==8:
        print("90%")                     # 진행률은 처음에 입력한 비교할 전체 회차 수 day중에서 i번째 반복을
        pass                             # i/day나누기로 표현해 백분율로 계산하여 표현
        per_cnt += 1                     # pass는 실시간 출력을 위해서이고
    elif i/day >= 0.8 and per_cnt==7:    # per_cnt는 10% 10% 10% ... 이런 중복 출력을 막기 위해서 필요하다.
        print("80%")                     # 결과를 보면 10% 20% 30% ... 이렇게 한번씩만 출력한다.
        pass
        per_cnt += 1
    elif i/day >= 0.7 and per_cnt==6:
        print("70%")
        pass
        per_cnt += 1
    elif i/day >= 0.6 and per_cnt==5:
        print("60%")
        pass
        per_cnt += 1
    elif i/day >= 0.5 and per_cnt==4:
        print("50%")
        pass
        per_cnt += 1
    elif i/day >= 0.4 and per_cnt==3:
        print("40%")
        pass
        per_cnt += 1
    elif i/day >= 0.3 and per_cnt==2:
        print("30%")
        pass
        per_cnt += 1
    elif i/day >= 0.2 and per_cnt==1:
        print("20%")
        pass
        per_cnt += 1
    elif i/day >= 0.1 and per_cnt==0:
        print("10%")
        pass
        per_cnt += 1
    
print(result)