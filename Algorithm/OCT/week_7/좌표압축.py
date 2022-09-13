n = int(input())
num_lst = list(map(int,input().split()))
cnt_set = set(num_lst)
cnt_lst = list(sorted(cnt_set))

for num in num_lst:
  print(cnt_lst.index(num), end=' ')

import sys
input = sys.stdin.readline

n = int(input())
num_lst = list(map(int,input().split()))
cnt_set = set(num_lst)
cnt_lst = list(sorted(cnt_set))
cnt_dic = dict()
for i in range(len(cnt_lst)):
  cnt_dic[cnt_lst[i]] = i

for num in num_lst:
  print(cnt_dic[num], end=' ')