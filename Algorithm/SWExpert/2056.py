# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
 



# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면

# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,

# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.


# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며

# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
 


# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)


# [입력]

# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

# 다음 줄부터 각 테스트 케이스가 주어진다.


# [출력]

# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

n = int(input())
for i in range(n):
    mon = input()
    lst_30 = ['04','06','09','11']
    if int(mon[4:6]) in range(1,13):
        if mon[4:6] in lst_30:
            if int(mon[6:8]) not in range(1,31):
                result = -1
            else:
                result = mon[0:4]+'/'+mon[4:6]+'/'+mon[6:8]
        elif mon[4:6] == '02':
            if int(mon[6:8]) not in range(1,29):
                result = -1
            else:
                result = mon[0:4]+'/'+mon[4:6]+'/'+mon[6:8]
        else:
            if int(mon[6:8]) not in range(1,32):
                result = -1
            else:
                result = mon[0:4]+'/'+mon[4:6]+'/'+mon[6:8]
    else:
        result = -1
    print(f'#{i+1} {result}')