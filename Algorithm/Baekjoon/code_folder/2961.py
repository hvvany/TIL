from itertools import combinations
answer = []
n = int(input())
c_lst = []
b_lst = []
for _ in range(n):
  c, b = map(int,input().split())
  c_lst.append(c)
  b_lst.append(b)

for selec in range(1,n+1):
  for sauce in combinations(range(n),selec):
    c_ans = 1
    b_ans = 0
    
    for idx in sauce:
      c_ans *= c_lst[idx]
      b_ans += b_lst[idx]
    answer.append(abs(c_ans - b_ans))
print(min(answer))