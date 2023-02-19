import math

n = int(input())
lst = list(map(int,input().split()))
answer = 0
for num in lst:
    if num == 1:
        continue
    if num == 2:
        answer += 1
        continue
    for 숫자 in range(2,math.ceil(math.sqrt(num)) + 1):
        if num % 숫자 == 0:
            break
    else:
        answer += 1
print(answer)