n, target = map(int,input().split())
money_lst = []
answer = 0
for _ in range(n):
    money_lst.append(int(input()))
for money in money_lst[::-1]:
    answer += target // money
    target %= money
    if target == 0:
        break
print(answer)