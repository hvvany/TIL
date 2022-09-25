# # 전체 넓이에서 작은 사각형 빼기
# n = int(input())
# inf_dic = dict()
# x, y = 2, 2
# w, h = 0, 0
# cut_w, cut_y = 0, 0
# for _ in range(6):
#   direction, long = map(int,input().split())
#   if direction not in inf_dic:
#     inf_dic[direction] = [long]
#   else:
#     inf_dic[direction] += [long]
#   print(inf_dic)
# for d in inf_dic:
#   if len(inf_dic[d]) == 2:
#     if d == 1:
#       y = 1
#     elif d == 2:
#       y = 0
#     if d == 3:
#       x = 1
#     elif d == 4:
#       x = 0
# for d in inf_dic:
#   if len(inf_dic[d]) == 2:
#     if d == 1 or d == 2:
#       cut_h = inf_dic[d][x]
#     else:
#       cut_w = inf_dic[d][y]
#   else:
#     if d == 1 or d == 2:
#       h = inf_dic[d][0]
#     else:
#       w = inf_dic[d][0]
# print(f'w : {w}, h : {h}, cw : {cut_w}, ch : {cut_h}')
# print((w*h-cut_w*cut_h)*n)




n = int(input())
lst = []
w, h = 0, 0
cut_lst = []
all_lst = []
inf_dic = dict()

for _ in range(6):
  d, long = map(int,input().split())
  if d in inf_dic:
    inf_dic[d] += [int(long)]
  else:
    inf_dic[d] = [int(long)]
  lst.append((d,long))
lst = lst + lst

print(f'lst : {lst}')
for i in range(6):
  if lst[i][0] == lst[i+2][0]:
    if lst[i+1][1] not in cut_lst:
      cut_lst.append(int(lst[i+1][1]))
for key in inf_dic:
  if len(inf_dic[key]) == 1:
    all_lst.append(inf_dic[key])

print((all_lst[0][0]*all_lst[1][0] - cut_lst[0]*cut_lst[1])*n)