'''
뒤에서 부터 하나씩 접근하여 
증가하면 매도 시기 최신화
감소하면 계속 매수 시기 최신화

'''

# # 스택
# import sys

# input = sys.stdin.readline

# n = int(input())
# sequence = list(map(int ,input().split()))
# stack = []
# answer = []

# for i, num in enumerate(sequence):
#   while stack and stack[-1] != num:
#     answer.append(i + 1)
#     stack.pop()
#   stack.append(num)

# while stack:
#   answer.append(-1)
#   stack.pop()
# print(*answer)

# ##############
# # 또 다른 버전 뒤로 돌리기
# import sys

# input = sys.stdin.readline

# n = int(input())
# A = list(map(int, input().split()))
# ans = [-1 for _ in range(n)]

# for i in range(n - 2, -1, -1):
#   if A[i] == A[i + 1]:
#     ans[i] = ans[i + 1]
#   else:
#     ans[i] = i + 2
# print(*ans)


# 뒤에서 부터 접근하여 이전 날이 높으면 파는날 최신화
# 떨어지면 사는날 최신화
# 사는날 파는날 짝이 지어지면 한 세트 완성
# [파는날, 사는날, 파는날, 사는날, 파는날......]
# 세트 완성 후 이번에는 앞에서 부터 접근
# 가격 보고 재산에서 코인 시세를 나눈 몫 만큼 살 수 있다

(days, money) = (map(int,input().split()))
# print(days,money)
lst = []
sell_buy_lst = []
for _ in range(days):
  lst.append(int(input()))

if days == 1:
  print(money)
elif days == 2:
  if lst[-1] > lst[-2]:
    print(money + (lst[-1]-lst[-2])*(money//lst[-2]))
  else:
    print(money)
else:
  if lst[-1] > lst[-2]:
    sell_buy_lst.append(-1)
  for i in range(2,days+1):
    if lst[-i] > lst[-i+1]:
      if i > 2 and lst[-i+1] <= lst[-i+2]:
        sell_buy_lst.append(-i+1)

    elif lst[-i] < lst[-i+1]:
      if i > 2 and lst[-i+1] >= lst[-i+2]:
        sell_buy_lst.append(-i+1)

    if i == days and lst[-i] <= lst[-i+1]:
      sell_buy_lst.append(-i)
  # print(sell_buy_lst)

  while sell_buy_lst:
    buy_day = sell_buy_lst.pop()
    buy_price = lst[buy_day]
    sell_day = sell_buy_lst.pop()
    sell_price = lst[sell_day]

    num_coin = money//buy_price
    money += (sell_price-buy_price)*num_coin
  print(money)