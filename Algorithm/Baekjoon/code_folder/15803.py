x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())

data_lst = [(x1,y1),(x2,y2),(x3,y3)]
n1 = abs(x3-x2)
n2 = abs(y3-y2)
d1 = abs(x2-x1)
d2 = abs(y2-y1)

if n1*d2 == n2*d1:
  print('WHERE IS MY CHICKEN?')
else:
  print('WINNER WINNER CHICKEN DINNER!')