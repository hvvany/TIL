lst = set()
t = int(input())
for _ in range(t):
  word = input()
  lst.add((len(word),word))
lst = sorted(lst)
for w in lst:
  print(w[1])