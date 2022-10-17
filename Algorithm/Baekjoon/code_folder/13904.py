import heapq
n = int(input())
lst = []
for _ in range(n):
  d, w = map(int,input().split())
  lst.append((-d,-w))
lst.sort()
score = 0
print(f'lst :{lst}')
i = -lst[0][0]
print(f'i : {i}')
memory = []
while lst:
  print(f'i : {i}')
  (d, w) = heapq.heappop(lst)
  print(f'(d,w) : {(d, w)}')
  if -d >= i:
    score += -w
    print(-w)
  else:
    heapq.heappush(lst,(d, w))
  i -= 1
  print(f'score:{score}') 

print(score)
# 일단 마감일 적은 순으로 접근하여 리스트 만들고
# 같은 마감일이면 따로 저장해놨다가 다시 돌면서 작은 값은 바꿔치기하기

