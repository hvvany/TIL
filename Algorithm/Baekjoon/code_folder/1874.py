import sys
input = sys.stdin.readline

n = int(input())
inform = []
stack = []
answer = ''
for _ in range(n):
  inform.append(int(input()))
breaker = False
k = 1
for target in inform:
  if breaker:
    break
  while True:
    if k == target:
      answer += '+-'
      k += 1
      break
    elif k < target:
      stack.append(k)
      answer += '+'
      k += 1
    else:
      before = stack.pop()
      if before == target:
        answer += '-'
        break
      else:
        answer = 'NO'
        breaker = True
        break
if answer == 'NO':
  print(answer)
else:
  for ans in answer:
    print(ans)