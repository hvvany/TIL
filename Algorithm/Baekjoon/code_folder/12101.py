from itertools import permutations
n, k = map(int,input().split())
num_lst = [1,2,3]
for count in range(1,n+1):
  per_lst = permutations(num_lst, count)
  for nums in per_lst:
    