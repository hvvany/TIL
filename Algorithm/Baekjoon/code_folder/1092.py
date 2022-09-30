import math
n = int(input())
c1, c2, c3 = map(int,input().split())
m = int(input())
box_lst = list(map(int,input().split()))
crane_dic = dict()
wow = True
for num in box_lst:
  if num > c3:
    print(-1)
    wow = False
    break
  elif c2 < num <= c3:
    crane_dic[c3] += 1
  elif c1 < num <= c2:
    crane_dic[c2] += 1
if wow:
  l = 0
  for num in crane_dic:
    if crane_dic[num] > l:
      l = crane_dic[num]
  print(f'l : {l}')
  print(f'c1 : {crane_dic[c1]},c2 : {crane_dic[c2]},c3 : {crane_dic[c3]}')
  if m < (l*3 - crane_dic[c2] - crane_dic[c3]):
    print(l)
  else:
    print(f'ceil :{(m-l*3)/3}')
    print(math.ceil((m-l*3)/3)+l)


# n = int(input())
# crane_lst = list(map(int,input().split()))
# m = int(input())
# box_lst = list(map(int,input().split()))
# crane_dic = dict()
# gdk = 0
# for num in box_lst:
#   if num > 





# import math
# n = int(input())
# crane_lst = list(map(int,input().split()))
# m = int(input())
# box_lst = list(map(int,input().split()))
# crane_lst.sort()
# box_lst.sort()
# print(f'crane : {crane_lst}, box_lst : {box_lst}')
