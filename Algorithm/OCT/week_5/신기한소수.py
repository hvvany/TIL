l = int(input())

자릿수 = 0
answer = []
is_sosu = True
def Sosu(before_num):
  global 자릿수
  global is_sosu
  자릿수 += 1
  for i in range(10):
    is_sosu = True
    cnt = 0
    new_num = int(str(before_num) + str(i))
    print(f'newnum : {new_num}')
    for num in range(2,10**(자릿수+1)):   # 시간 초과가 난다면 2의 배수는 따로 해주기
      if new_num % num == 0: 
        cnt += 1
        if cnt == 2:           # 자기 자신 제외한 나누기 가능 : 소수가 아닌것이 들통남
          is_sosu = False
          print(f'is_sosu : {is_sosu}')
          break                # 다음 i 로 넘어감
    print(f'for is_sosu : {is_sosu}')
    if is_sosu == True:
      print('True')
      if 자릿수 == l:   
        answer.append(new_num)
      else:
        print(f'else')
        Sosu(new_num)

Sosu(0)
print(answer)

