n = int(input())

k1 = n // 5
k2 = n // 3
k3 = n % 5
k4 = n % 3

n5 = k1
n3 = 0

if k1 != 0:
  if k3 == 4:
    if n5 >= 1:
      n5 -= 1
      n3 += 3
    else:
      n5 = -1
  elif k3 == 3:
    n3 += 1
  elif k3 == 2:
    if n5 >= 2:
      n5 -= 2
      n3 += 4
    else:
      n5 = -1
  elif k3 == 1:
    if n5 >= 1:
      n5 -= 1
      n3 += 2
    else:
      n5 = -1
else:
  if k3 == 3:
    n3 += 1
  else:
    n5 = -1
print(n3 + n5)
print(f'n3 : {n3}, n5 : {n5}')
