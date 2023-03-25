# 거북이
# https://www.acmicpc.net/problem/8911

T = int(input())
for _ in range(T):
  x_min, x_max, y_min, y_max = 0,0,0,0
  # 현재 바라보는 방향 : N, S, E, W
  now = [0,0,'N']
  order_lst = list(input())
  for order in order_lst:
    if order == 'F':
      if now[2] == 'N':
        now[0] += 1
      elif now[2] == 'S':
        now[0] -= 1
      elif now[2] == 'E':
        now[1] += 1
      elif now[2] == 'W':
        now[1] -= 1
        
    elif order == 'B':
      if now[2] == 'N':
        now[0] -= 1
      elif now[2] == 'S':
        now[0] += 1
      elif now[2] == 'E':
        now[1] -= 1
      elif now[2] == 'W':
        now[1] += 1
        
    elif order == 'L':
      if now[2] == 'N':
        now[2] = 'W'
      elif now[2] == 'E':
        now[2] = 'N'
      elif now[2] == 'S':
        now[2] = 'E'
      elif now[2] == 'W':
        now[2] = 'S'
      
    elif order == 'R':
      if now[2] == 'N':
        now[2] = 'E'
      elif now[2] == 'E':
        now[2] = 'S'
      elif now[2] == 'S':
        now[2] = 'W'
      elif now[2] == 'W':
        now[2] = 'N'

    if now[0] < x_min:
      x_min = now[0]
    elif now[0] > x_max:
      x_max = now[0]
    if now[1] < y_min:
      y_min = now[1]
    elif now[1] > y_max:
      y_max = now[1]
  print((x_max - x_min)*(y_max - y_min))