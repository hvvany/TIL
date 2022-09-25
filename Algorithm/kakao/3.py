from itertools import *

def solution(users, emoticons):
    sale = [10,20,30,40]
    sale_List = list(product(sale, repeat = len(emoticons)))

    inform_lst = []

    for sale_inf in sale_List:
      user_pay_total = 0
      kakao_plus_cnt = 0
      for user in users:
        user_pay = 0
        for i in range(len(emoticons)):
          if user[0] <= sale_inf[i]:
            user_pay += emoticons[i] * ((100-sale_inf[i])/100)

        if user_pay >= user[1]:
          kakao_plus_cnt += 1
        else:
          user_pay_total += user_pay

      inform_lst.append([kakao_plus_cnt,int(user_pay_total)])
    inform_lst.sort()
    return inform_lst[-1]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))