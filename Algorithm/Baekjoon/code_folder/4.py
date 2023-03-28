# 전구와 스위치
# https://www.acmicpc.net/problem/2138

n = int(input())
before_lst = list(input())
target_lst = list(input())
trans_lst = []
for i in range(len(before_lst)):
  if before_lst[i] == target_lst[i]:
    trans_lst.append(0)
  else:
    trans_lst.append(1)
answer = 0
for i in range(len(trans_lst)-1):
  if trans_lst[i] == 1:
    for idx in range(3):
      if i + idx < len(trans_lst):
        trans_lst[i+idx] = (trans_lst[i+idx] + 1) % 2
    answer += 1
if trans_lst[:3] == [0,0,1] or trans_lst[:3] == [1,1,0]:
  answer += 1
  trans_lst[:3] == [0,0,0]
elif trans_lst[-3:] == [1,0,0] or trans_lst[-3:] == [0,1,1]:
  answer += 1
  trans_lst[-3:] == [0,0,0]
if 1 in trans_lst[-3:]:
  print(-1)
else:
  print(answer)