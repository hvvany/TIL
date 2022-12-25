import math
n = int(input())
m = int(input())
position = list(map(int,input().split()))
answer = set()
if len(position) > 1:
    for i in range(len(position) - 1):
        distance = position[i+1] - position[i]
        answer.add(math.ceil(distance / 2))
answer.add(position[0])
answer.add(n-position[-1])
print(max(answer))