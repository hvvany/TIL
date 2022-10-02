n = int(input())
lst_in = dict()
lst_out = []
cnt = 0

for i in range(n):
  lst_in[input()] = i
for _ in range(n):
  lst_out.append(lst_in[input()])
for j in range(n):
  for num in lst_out[j:]:
    if num < lst_out[j]:
      cnt += 1
      break
print(cnt)