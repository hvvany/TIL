# 입력 받은 수에서 1씩 빼가며 4,7 로만 구성되면 프린트

n = int(input())
breaker = False
while True:
    cnt = 0
    for num in str(n):
        if num == '4' or num == '7':
            cnt += 1
            if cnt == len(str(n)):
                breaker = True
                break
        else:
            break
    if breaker == True:
        break
    n -= 1
print(n)