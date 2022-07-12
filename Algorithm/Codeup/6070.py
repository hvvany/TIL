# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

# 예시
# ...
# if n//3==1 :
#   print("spring")
# ...

month = int(input())
if month // 3 == 1:
    print('spring')
elif month // 3 == 2:
    print('summer')
elif month // 3 == 3:
    print('fall')
else:
    print('winter')

