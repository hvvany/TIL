yt, yj = map(int,input().split())
while True:
  if yt >= 5:
    print('yj')
    break
  elif yj >= 5:
    print('yt')
    break
  yj += yt
  if yt >= 5:
    print('yj')
    break
  elif yj >= 5:
    print('yt')
    break
  yt += yj