n, k = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()
cnt = 0
i = 0
if k == 1:
  print(len(lst))
else:
  while True:
    next_num = lst[i] + k - 1
    if next_num >= lst[-1]:
      cnt += 1
      break
    for j in range(i,n):
      if lst[j] > next_num:
        cnt += 1
        i = j
        break
  print(cnt)