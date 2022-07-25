

## 1일차

| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 2558      | A + B - 2 |

#### 문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

#### 예시 입력

```output
1
2
```

#### 예시 출력

```output
3
```

#### 제출

```python
a = int(input())
b = int(input())
print(a+b)
```



---

## 

| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 10953     | A + B - 6 |

#### 문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

#### 예시 입력

```output
5
1,1
2,3
3,4
9,8
5,2
```

#### 예시 출력

```output
2
5
7
17
7
```

#### 제출

```python
n = int(input())
for i in range(n):
    num_lst = list(map(int,input().split(',')))
    print(sum(num_lst))
```



---

## 

| 문제 번호 | 문제 이름    |
| --------- | ------------ |
| 10995     | 별 찍기 - 20 |

#### 문제

예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

#### 예시 입력

```output
1

2

4
```

#### 예시 출력

```output
*

* *
 * *
 
* * * *
 * * * *
* * * *
 * * * *
```

#### 제출

```python
n = int(input())
star = '* '
for i in range(n):
    if i%2 == 0:
        txt = star*n
        print(txt.rstrip())
    else:
        txt = star[::-1]*n
        print(txt.rstrip())
```



---

## 

| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 1065      | 한 수     |

#### 문제

어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

#### 예시 입력

```output
110

1000

500
```

#### 예시 출력

```output
99

144

119
```

#### 제출

```python
# 한 수 : 자릿수가 등차수열
# 등차수열이므로 등차 dif 를 구한다.
# 등차수열 공식 a + (n-1)*d 를 통해 len(num)=n 까지의 수열을 문자열로 덧붙이기
# 문자열을 정수로 변환하여 숫자 비교
# 결국 초기값 a = int(num[0]) 이고 d = map(int, num[i]-num[i+1]), n = len(num)
# 같으면 한수 카운트 cnt 증가

num_in = input()
dif = 0                                  # 연속된 두 인덱스 숫자 차이 크기 초기값
cnt = 0                                  # 한 수 개수 초기값

for num in range(1,int(num_in)+1):             
    if num < 10 :                       # 한 자릿수는 바로 출력
        cnt = num
    else:
        dif = int(str(num)[1])-int(str(num)[0])           # 등차 크기
        num_comp = ''                            # 비교 할 숫자 초기값 ''(빈 문자열)                  
        for n in range(1,len(str(num))+1):            # n은 등차수열 개수로써 num의 자릿수(len(num))이다.
            num_comp += str(int(str(num)[0]) + (n-1)*dif)  # 문자열에 순서대로 값 추가  (a + (n-1)d )
        if str(num) == num_comp:
            cnt += 1                # 등차수열과 같으면 cnt 추가

print(cnt)
```

