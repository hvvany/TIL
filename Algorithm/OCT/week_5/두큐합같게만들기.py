# 두 큐의 합 구한 후 절반 나누기
# 절반 값 보다 큰 큐에서 pop 해서 append(pop(0))
# 다시 계산
from collections import deque
def solution(queue1, queue2):
  queue1 = deque(queue1)
  queue2 = deque(queue2)

  cnt = 0
  q1_sum = sum(queue1)
  q2_sum = sum(queue2)
  n = 3*len(queue1)

  breaker = False
  while cnt < n:
    if q1_sum < q2_sum:   # q1 이 작은 큐인 경우
      pop_2 = queue2.popleft()
      queue1.append(pop_2)
      q1_sum += pop_2
      q2_sum -= pop_2
      cnt += 1
      print(f'q1 작은 경우\n q1 : {queue1} q2 : {queue2} cnt : {cnt} q1_sum : {q1_sum} q2_sum : {q2_sum}')
    elif q1_sum > q2_sum:   # q1 이 큰 큐인 경우
      pop_1 = queue1.popleft()
      queue2.append(pop_1)
      q2_sum += pop_1
      q1_sum -= pop_1
      cnt += 1
      print(f'q1 큰 경우\n q1 : {queue1} q2 : {queue2} cnt : {cnt} q1_sum : {q1_sum} q2_sum : {q2_sum}')
    elif q1_sum == q2_sum:
      breaker = True
      break
  if breaker == True:
    answer = cnt
  else:
    answer = -1

  return answer

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
print(solution(queue1, queue2))