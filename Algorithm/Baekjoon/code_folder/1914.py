import sys
input = sys.stdin.readline

def hanoi(cnt,f,temp,t):
  if cnt == 0:
    return
  else:
    hanoi(cnt-1, f,t,temp)
    answer.append((f,t))
    hanoi(cnt-1,temp,f,t)
    
answer = []   
n = int(input())
hanoi(n,1,2,3)
print(len(answer))
for num in answer:
  print(*num)