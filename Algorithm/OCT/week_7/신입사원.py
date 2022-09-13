# 각 1등은 무조건 뽑힌다. 2명 기본
# 1등의 나머지 다른 순위 보다 낮으면 탈락.
# n = int(input())

# for _ in range(n):
#   score_lst = []
#   death_note = set()
#   max_a, max_b = 0, 0

#   person = int(input())
#   for i in range(person):
#     (a,b) = tuple(map(int,input().split()))
#     score_lst.append((a,b))

#   for score in score_lst:
#     print(f'score[0] : {score[0]} score[1] : {score[1]}')
#     if score[0] == 1:
#       max_b = score[1]     # 첫 점수 1등의 두 번째 등수 기록
#     if score[1] == 1:    
#       max_a = score[0]     # 두 번째 점수 1등의 첫 번째 등수 기록
#   print(f'a: {max_a}, b : {max_b}')
#   print(score_lst)
  
#   for i in range(len(score_lst)):
#     # print(f'score[0] : {score[0]} score[1] : {score[1]}')
#     if score_lst[i][0] > max_a or score_lst[i][1] > max_b:
#       death_note.add(i)
#   print(person - len(death_note))


n = int(input())

for _ in range(n):
  rank_lst = []
  person = int(input())
  second_rank = person + 1
  cnt = 0

  for i in range(person):
    (a,b) = tuple(map(int,input().split()))
    rank_lst.append((a,b))

  rank_sort_lst = sorted(rank_lst,key=lambda x : x[0])
  # print(f'rank_sort_lst : {rank_sort_lst}')

  for i in range(person):
    if rank_sort_lst[i][1] < second_rank:
      second_rank = rank_sort_lst[i][1]
      # print(f'second_rank : {second_rank}')
      cnt += 1
  print(cnt)