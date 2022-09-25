t = int(input())

dic = dict()
cnt_lst = []
lst = []
s = 0

for _ in range(t):
  k = int(input())
  lst.append(k)
  s += k
  if k in dic:
    dic[k] += 1
  else:
    dic[k] = 1
for number in dic:
  cnt_lst.append([dic[number],number])
cnt_lst.sort()
lst.sort()
num = int(round(s/t,0))
print(num)
print(lst[(t-1)//2])
m = cnt_lst[-1][1]
bindo = []
for i in range(len(cnt_lst)):
  if cnt_lst[-i-1][0] == cnt_lst[-1][0]:
    bindo.append(cnt_lst[-i-1][1])
bindo.sort()
if len(bindo) > 1:
  print(bindo[1])
else:
  print(bindo[0])
print(lst[-1]-lst[0])