n = int(input())
lst = []
for _ in range(n):
  lst.append(int(input()))
for n in sorted(lst):
  print(n)