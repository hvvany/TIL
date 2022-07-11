# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.

a, b = input().split()

a_int, b_int = int(a), int(b)
# a_f, b_f = float(a), float(b)
print(a_int+b_int)
print(a_int-b_int)
print(a_int*b_int)
print(a_int//b_int)
print(a_int%b_int)
print(format(a_int/b_int, '.2f'))