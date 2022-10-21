n = int(input())
lst = []

for _ in range(n):
  lst.append(int(input()))
score = lst[-1]
answer = 0
for i in range(n):
  now_point = lst[-1-i]
  if now_point-score < 0:
    # print(f'if now_p :{now_point}, score :{score}')
    answer += i*(score-now_point)
    score = now_point -1
  else:
    # print(f'else now_p :{now_point}, score :{score}')
    answer += (now_point - score)
    score -= 1
  # print(f'answer : {answer} score : {score}')
print(answer)