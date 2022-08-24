import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  breaker = False
  order = input()
  n = int(input())
  str_lst = input()
  if n == 0:
    print('error')
    continue
  lst = list(map(int,str_lst[1:-2].split(',')))
  rev_mod = 1
  for ord in order:
    if ord == 'R':
      rev_mod *= -1
    elif ord == 'D':
      if len(lst) == 0:
        print('error')
        breaker = True
        break
      else:
        if rev_mod == 1:
          lst.pop(0)
        else:
          lst.pop(-1)
  if breaker == True:
    continue
  print(str(lst[::rev_mod]).replace(' ',''))