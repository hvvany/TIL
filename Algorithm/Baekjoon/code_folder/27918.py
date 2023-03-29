import sys
def solution():
  passer = False
  input = sys.stdin.readline
  N = int(input())
  d, p = 0, 0
  for _ in range(N):
    inform = input().rstrip()
    if passer:
      continue
    if inform == 'D':
      d += 1
    else:
      p += 1
    if abs(d-p) == 2:
      print(f'{d}:{p}')
      passer = True
  if not passer:
    print(f'{d}:{p}')
  return
solution()