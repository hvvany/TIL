lst = list(input())
answer = ''
for number in sorted(lst,reverse=True):
  answer += number
print(answer)