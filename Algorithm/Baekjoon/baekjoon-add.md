

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



---



| 문제 번호 | 문제 이름               |
| --------- | ----------------------- |
| 2609      | 최대공약수와 최소공배수 |

#### 문제

두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

#### 예시 입력

```output
24 18
```

#### 예시 출력

```output
6
72
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



---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 2231      | 분해합    |

#### 문제

어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

#### 예시 입력

```output
216
```

#### 예시 출력

```output
198
```

#### 제출

```python
# 숫자 범위는 입력한 숫자 에서 9*len(입력숫자) 뺀 숫자까지
# 1씩 증가시키며 조건 충족하는지 확인
# 조건 충족시키는 값은 리스트에 저장해서 최소값 출력

num = input()
maker_lst = []

for maker in range(1,int(num)):
    num_sum = []
    for i in str(maker):
        num_sum.append(int(i))
    num_sum.append(maker)
    if sum(num_sum) == int(num):
        maker_lst.append(maker)

if sum(maker_lst) == 0:
    maker_lst=[0]
print(min(maker_lst))
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 2846      | 오르막길  |

#### 문제

상근이는 자전거를 타고 등교한다. 자전거 길은 오르막길, 내리막길, 평지로 이루어져 있다. 상근이는 개강 첫 날 자전거를 타고 가면서 일정 거리마다 높이를 측정했다. 상근이는 가장 큰 오르막길의 크기를 구하려고 한다.

측정한 높이는 길이가 N인 수열로 나타낼 수 있다. 여기서 오르막길은 적어도 2개의 수로 이루어진 높이가 증가하는 부분 수열이다. 오르막길의 크기는 부분 수열의 첫 번째 숫자와 마지막 숫자의 차이이다.

예를 들어, 높이가 다음과 같은 길이 있다고 하자. 12 3 5 7 10 6 1 11. 이 길에는 2 개의 오르막길이 있다. 밑 줄로 표시된 부분 수열이 오르막길이다. 첫 번째 오르막길의 크기는 7이고, 두 번째 오르막길의 크기는 10이다. 높이가 12와 6인 곳은 오르막길에 속하지 않는다.

가장 큰 오르막길을 구하는 프로그램을 작성하시오.

#### 예시 입력

```output
5
1 2 1 4 6

8
12 20 1 3 4 4 11 1

6
10 8 8 6 4 3
```

#### 예시 출력

```output
5

8

0
```

#### 제출

```python
# 측정 횟수 입력
# 수열 입력
# 횟수만큼 반복하며 수열 리스트 하나씩 꺼내서 이전 숫자와 감소면 길이 변수 초기화
# while 증가면 리스트에 숫자 두 개 계속 추가하여 while 끝나고 맨앞과 맨뒤 차이 리스트에 저장

n = int(input())
regit_lst = list(map(int,input().split()))
height_lst = []
height = 0
for i in range(n-1):
    if regit_lst[i] < regit_lst[i+1]:
        height += regit_lst[i+1]-regit_lst[i]
        i += 1
    else:
        height_lst.append(height)
        height = 0
    height_lst.append(height)
print(max(height_lst))
```

 

---



| 문제 번호 | 문제 이름     |
| --------- | ------------- |
| 2953      | 나는 요리사다 |

#### 문제

"나는 요리사다"는 다섯 참가자들이 서로의 요리 실력을 뽐내는 티비 프로이다. 각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다. 점수는 1점부터 5점까지 있다.

각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.

각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

#### 예시 입력

```output
5 4 4 5
5 4 4 4
5 5 4 4
5 5 5 4
4 4 4 5

4 4 3 3
5 4 3 5
5 5 2 4
5 5 5 1
4 4 4 4
```

#### 예시 출력

```output
4 19

2 17
```

#### 제출

```python
score_lst = []
for i in range(5):
    score_sum = sum(list(map(int, input().split())))
    score_lst.append(score_sum)
print(score_lst.index(max(score_lst))+1, max(score_lst))
```

 





