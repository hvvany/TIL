n = int(input())
lst = list(input())
l = len(lst)
memory = ['']*l
next_lst = ['']*l
cnt = 0
n %= l
while cnt < n:
  k, idx = 1, 0
  for i in range(l):
    next_lst[idx*k] = lst[i]
    k *= -1
    idx -= i % 2
    idx += 1
  cnt += 1
  print(lst)
  lst = next_lst.copy()
print(''.join(next_lst))