n = int(input())
for _ in range(n):
  cnt = 0
  a, b, c = map(int,input().split())
  if a >= 10:
    cnt += 1
  if b >= 10:
    cnt += 1
  if c >= 10:
    cnt += 1
  print(a,b,c)
  if cnt == 3:
    print('triple-double')
  elif cnt == 2:
    print('double-double')
  elif cnt == 1:
    print('double')
  else:
    print('zilch')
  print()