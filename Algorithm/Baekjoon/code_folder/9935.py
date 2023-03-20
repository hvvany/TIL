import sys
input = sys.stdin.readline

str_inform = list(input().rstrip())
bomb = input().rstrip()
idx_checker = 0
while idx_checker < len(str_inform):
  if str_inform[idx_checker] == bomb[0]:
    bomb_pop = True
    idx_checker_start = idx_checker
    idx_bomb = 0
    while idx_bomb < len(bomb):
      if str_inform[idx_checker] == bomb[idx_bomb]:
        idx_checker += 1
        idx_bomb += 1
        continue
      elif str_inform[idx_checker] == '!':
        idx_checker += 1
        continue
      else:
        bomb_pop = False
        idx_checker -= 1
        break
    if bomb_pop:
      idx_checker = idx_checker_start
      idx_bomb = 0
      while idx_bomb < len(bomb):
        if str_inform[idx_checker] == bomb[idx_bomb]:
          str_inform[idx_checker] = '!'
          idx_checker += 1
          idx_bomb += 1
        elif str_inform[idx_checker] == '!':
          idx_checker += 1
      idx_checker = idx_checker_start - len(bomb)
  idx_checker += 1
answer = ''
for inform in str_inform:
  if inform != '!':
    answer += inform
if len(answer) == 0:
  print('FRULA')
else:
  print(answer)