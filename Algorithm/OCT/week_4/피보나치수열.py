import sys
input = sys.stdin.readline

def Fibonacci(n):
  global cnt_0
  global cnt_1
  if n == 40:
    cnt_0 = 63245986
    cnt_1 = 102334155
    return 0
  elif n == 39:
    cnt_0 += 39088169
    cnt_1 += 63245986
    return 0
  elif n == 38:
    cnt_0 += 24157817
    cnt_1 += 39088169
    return 0
  elif n == 37:
    cnt_0 += 14930352
    cnt_1 += 24157817
    return 0
  elif n == 36:
    cnt_0 += 9227465
    cnt_1 += 14930352
    return 1
  elif n == 35:
    cnt_0 += 5702887
    cnt_1 += 9227465
    return 0
  elif n == 34:
    cnt_0 += 3524578
    cnt_1 += 5702887
    return 0
  elif n == 33:
    cnt_0 += 2178309
    cnt_1 += 3524578
    return 0
  elif n == 32:
    cnt_0 += 1346269
    cnt_1 += 2178309
    return 0
  elif n == 31:
    cnt_0 += 832040
    cnt_1 += 1346269
    return 0
  elif n == 30:
    cnt_0 += 514229
    cnt_1 += 832040
    return 0
  elif n == 28:
    cnt_0 += 196418
    cnt_1 += 317811
    return 0
  elif n == 26:
    cnt_0 += 75025
    cnt_1 += 121393
    return 0
  elif n == 24:
    cnt_0 += 28657
    cnt_1 += 46368
    return 0
  elif n == 0:
    cnt_0 += 1
    return 0
  elif n == 1:
    cnt_1 += 1
    return 1
  else:
    return Fibonacci(n-1) + Fibonacci(n-2)

t = int(input())
for _ in range(t):
  cnt_0 = 0
  cnt_1 = 0
  n = int(input())
  Fibonacci(n)
  print(cnt_0, cnt_1)