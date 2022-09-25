import math

w, h, x, y, p = map(int,input().split())
r = h/2
person_lst = []
cnt = 0
for _ in range(p):
  person_lst.append(tuple(map(int,input().split())))

for person in person_lst:
  (i,j) = person
  # 사각형 내부 존재
  if x <= i <= x+w and y <= j <= y+h:
    cnt += 1
  # 사각형 외부 왼쪽 존재
  
  elif math.sqrt((x-i)**2 +(y+r-j)**2) <= r:
    cnt += 1
  # 사각형 외부 오른쪽 존재
  elif math.sqrt((x+w-i)**2 +(y+r-j)**2) <= r:
    cnt += 1
print(cnt)