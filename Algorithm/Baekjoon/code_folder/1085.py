matrix = list(map(int,input().split()))
[x,y,w,h] = matrix
answer = [x,y,w-x,h-y]
print(min(answer))