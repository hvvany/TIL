import sys
input = sys.stdin.readline

from itertools import product
n, k = map(int,input().split())
num_lst = [1,2,3]
answer_lst = []
for count in range(1,n+1):
  per_lst = product(num_lst,repeat=count)
  for nums in per_lst:
    if sum(nums) == n:
      answer_lst.append(nums)
answer_lst.sort()
try:
  for idx in range(len(answer_lst[k - 1])-1):
    print(answer_lst[k - 1][idx],end='+')
  print(answer_lst[k-1][-1])
except:
  print(-1)