from django.shortcuts import render
import random
import datetime
import requests

# Create your views here.
def lotto_num(request):
  num_lst = []
  for n in range(1,46):
      num_lst.append(n)
  number = random.sample(num_lst,6)
  number.sort()



  rank = 0

  day_now = datetime.date.today()
  day_init = datetime.date(2022,7,16)  # 1024회 기준 날짜. 기준 날짜를 바탕으로 최신 회차 계산
  day_dif = day_now - day_init    
  day = int(1024+int((day_dif.days-1)/7))

  #회차별 데이터 불러오기
  url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={day}'
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
      if num in number:    # 뽑은 숫자와 메인볼 비교
          score += 2         # 메인볼과 같으면 score 2점 추가
  if bonus in number:      # 보너스 볼이면 score 1점만 추가
      score += 1

  # 등수 계산
  if score >= 12:            # 1등이면 메인볼 6개 이므로 총 12점
      rank = 1              # 1등 당첨 횟수 누적기록
  elif score >= 11:          # 2등이면 메인볼 5개 보너스볼 1개 11점
      rank = 2               # 2등 당첨 횟수 누적기록
  elif score >= 10:          # 3등이면 메인볼 5개
      rank = 3              # 3등 당첨 횟수 누적기록
  elif score >= 8:           # 4등이면 메인볼 4개
      rank = 4               # 4등 당첨 횟수 누적기록
  elif score >= 6:           # 5등이면 메인볼 3개
      rank = 5       

  context = {
    'rank' : rank,
    'b1' : number[0],
    'b2' : number[1],
    'b3' : number[2],
    'b4' : number[3],
    'b5' : number[4],
    'b6' : number[5],
  }

  return render(request,'index.html',context)
