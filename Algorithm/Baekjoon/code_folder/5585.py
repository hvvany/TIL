money = int(input())
left = 1000 - money
answer = 0
money_lst = [500, 100, 50, 10, 5, 1]
for num in money_lst:
    answer += left//num
    left = left%num
print(answer)