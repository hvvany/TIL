n = int(input())
cnt = 0

for _ in range(n):
  word_memory = []
  word = input()
  group_word = True
  if len(word) == 1:
    cnt += 1
    continue
  else:
    for i in range(len(word)-1):
      if word[i] in word_memory:
        group_word = False
        break
      else:
        if word[i] != word[i+1]:
          word_memory.append(word[i])
    if word[-1] in word_memory:
      group_word = False
    if group_word == True:
      cnt += 1
print(cnt)