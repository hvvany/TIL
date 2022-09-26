# 인접한 두 수 차이를  구해서 가장 큰 수 두 개를 분기접으로 나누기
# 같은 차이라면 모든 포인트를 돌면서 최대인지 확인?해서 선정
# import sys
# input = sys.stdin.readline

# n, k = map(int,input().split())
# lst = list(map(int,input().split()))
# dif_lst = []
# answer = 0

# for i in range(1,n):
#   dif_lst.append(lst[i]-lst[i-1])

# dif_sort = sorted(dif_lst)
# dif_dic = dict()
# for j in dif_sort[1-k:]:
#   dif_dic[j] = dif_dic.get(j,0) + 1
# # print(f'dif_dic : {dif_dic}')

# cut_idx = 0
# for i in range(n-1):
#   num = dif_lst[i]
#   if num in dif_dic:
#     if dif_dic[num] != 0:
#       answer += lst[i] - lst[cut_idx]
#       print(f'slice : [{cut_idx} : {i}]')
#       cut_idx = i+1
#       dif_dic[num] -= 1
# answer += (lst[n-1] - lst[cut_idx])
# print(f'slice : [{cut_idx} : {n-1}]')
# print(answer)




import sys
input = sys.stdin.readline

n, k = map(int,input().split())
lst = list(map(int,input().split()))
dif_lst = []

if k == 1:
  print(lst[-1] - lst[0])
else:
  for i in range(1,n):
    dif_lst.append(lst[i]-lst[i-1])

  dif_sort = sorted(dif_lst)
  dif_sort[1-k:] = [0]*(1-k)
  print(sum(dif_sort))