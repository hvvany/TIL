import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int,input().split())
beer_lst = []

for _ in range(k):
  pre, alc = map(int,input().split())
  beer_lst.append((alc,-pre))
beer_lst.sort(reverse=True)
                        # beer_lst : [(6, -4), (5, -2), (4, -1), (3, -3), (3, -4)]

no_answer = True
prefer_lst = []                            # n=3 m=9 k=5
prefer_score = 0

while beer_lst:                         # beer_lst 값이 있는동안 반복 (하나씩 pop)
  (answer, score) = beer_lst.pop()         # (3, -4)
  heapq.heappush(prefer_lst,-score)        # prefer_lst :[4]
  prefer_score -= score                    # prefer_score : 4
  if len(prefer_lst) >= n:                 # 축제 기간 이상의 길이를 가지면  
    if prefer_score >= m:                     # 선호도 만족하면
      print(answer)                              # answer 출력
      no_answer = False
      break
    else:                                     # 선호도 불만족
      rm = heapq.heappop(prefer_lst)             # 삭제 대상 삭제 (가장 작은 값)
      prefer_score -= rm                         # prefer_score 도 빠진 만큼 빼주기

if no_answer:                              # 노답이면  -1출력
  print(-1)
'''
prefer_lst :[4]
prefer_score : 4

prefer_lst :[3, 4]
prefer_score : 7

prefer_lst :[1, 4, 3]
prefer_score : 8

prefer_lst :[2, 4, 3]
prefer_score : 9
'''