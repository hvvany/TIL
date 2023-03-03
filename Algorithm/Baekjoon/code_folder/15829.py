import sys
input = sys.stdin.readline

n = int(input())
lst = list(input())
answer = 0
for i in range(n):
  answer += (ord(lst[i])-ord('a')+1)*31**i
print(answer)