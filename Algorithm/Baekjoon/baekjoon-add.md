

## 

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

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 2789      | 유학 금지 |

#### 문제

아주 멀리 떨어져 있는 작은 나라가 있다. 이 나라에서 가장 공부를 잘하는 학생들은 모두 다른 나라로 유학을 간다. 정부는 최고의 학생들이 자꾸 유학을 가는 이유를 찾으려고 했다. 하지만, 학생들의 이유가 모두 달랐기 때문에 정확한 이유를 찾을 수 없었다. 정부의 고위직은 뛰어난 학생들이 자꾸 유학을 가는 현상을 매우 불쾌해 했다.

가장 많은 학생들이 유학을 가는 대학교는 영국의 캠브리지 대학교이다. 정부는 인터넷 검열을 통해서 해외로 나가는 이메일의 내용 중 일부를 삭제하기로 했다. 이메일의 각 단어 중에서 CAMBRIDGE에 포함된 알파벳은 모두 지우기로 했다. 즉, 어떤 이메일에 LOVA란 단어가 있다면, A는 CAMBRIDGE에 포함된 알파벳이기 때문에, 받아보는 사람은 LOV로 받는다.

이렇게, 어떤 단어가 주어졌을 때, 검열을 거친 후에는 어떤 단어가 되는지 구하는 프로그램을 작성하시오.

#### 예시 입력

```output
LOVA

KARIJERA
```

#### 예시 출력

```output
LOV

KJ
```

#### 제출

```python
text = list(' '.join(input()).split())
for i in range(len(text)):
    if text[i] in 'CAMBRIDGE':
        text[i] = ''
for i in text:
    print(i,end="")
```

 



---



| 문제 번호 | 문제 이름       |
| --------- | --------------- |
| 17249     | 태보태보 총난타 |

#### 문제

태보(TaeBo)란, 태권도와 복싱을 조합한 운동이다. 복싱의 공격 기술로는 민첩하게 앞주먹을 뻗으면서 가볍게 치는 잽, 옆으로 치는 펀치인 훅이 있다.

선풍적인 인기에 태보 강의를 들으며 태보를 마스터한 혜정이는 이제 펀치 속도가 워낙 빨라서 잽과 훅을 반복하다보면 잔상이 남는다.

얼굴의 왼편에 왼손의 잔상이, 오른편에는 오른손이 잔상이 남을 때 혜정이는 주먹을 몇 번 뻗었을까?

주먹의 잔상은 =로 시작하여 @로 끝나고, 잔상이 남지 않는 경우는 없다. 얼굴 형태가 (^0^) 꼴이고, 주먹의 잔상이 같은 곳에 위치하지 않는다.

#### 예시 입력

```output
@===@==@=@==(^0^)==@=@===@
```

#### 예시 출력

```output
4 3
```

#### 제출

```python
tb = input()
center_idx = tb.index('0')
print(tb[:center_idx-2].count('@'),tb[center_idx+3:].count('@'))
```

 



---



| 문제 번호 | 문제 이름     |
| --------- | ------------- |
| 2711      | 오타맨 고창영 |

#### 문제

고창영은 맨날 오타를 낸다. 창영이가 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때, 오타를 지운 문자열을 출력하는 프로그램을 작성하시오.

창영이는 오타를 반드시 1개만 낸다.

#### 예시 입력

```output
4
4 MISSPELL
1 PROGRAMMING
7 CONTEST
3 BALLOON
```

#### 예시 출력

```output
MISPELL
ROGRAMMING
CONTES
BALOON
```

#### 제출

```python
# 오타 낸다고?
# 오타낸 위치 (인덱스 +1 ) 문자열 입력
# 리스트로 값을 받고 인덱스1에 문자열 접근하여 replace로 print? -> replace는 해당 알파벳 모두 삭제!
# 그냥 인덱스로 접근해서 공백으로 없애버리는 방법

t = int(input())
for i in range(t):
    text = list(input().split())
    for idx in range(len(text[1])):
        if idx == int(text[0])-1:
            continue
        print(text[1][idx],end='')
    print()
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 2920      | 음계      |

#### 문제

다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

#### 예시 입력

```output
1 2 3 4 5 6 7 8

8 7 6 5 4 3 2 1

8 1 7 2 6 3 5 4
```

#### 예시 출력

```output
ascending

descending

mixed
```

#### 제출

```python
# '12345678' 순서대로면 ascending 반대면 descending, 혼합이면 mixed
# 입력받은 text 리스트 순서대로 꺼내붙여서 비교

text = input().split()
eum = ''
asc = '12345678'
for t in text:
    eum += t
if eum == asc:
    print('ascending')
elif eum == asc[::-1]:
    print('descending')
else:
    print('mixed')
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 4673      | 셀프 넘버 |

#### 문제

셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.

양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다. 

예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.

33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...

n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다. 

생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97

10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

#### 예시 입력

```output
입력은 없다.
```

#### 예시 출력

```output
1
3
5
7
9
20
31
42
53
64
 |
 |       <-- a lot more numbers
 |
9903
9914
9925
9927
9938
9949
9960
9971
9982
9993
```

#### 제출

```python
except_lst = []

for n in range(10001):
    except_lst.append(n+sum(map(int,str(n))))
for num in range(10001):
    if num not in except_lst:
        print(num)
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 2511      | 카드놀이  |

#### 문제

0부터 9까지의 숫자가 표시된 카드를 가지고 두 사람 A와 B가 게임을 한다. A와 B에게는 각각 0에서 9까지의 숫자가 하나씩 표시된 10장의 카드뭉치가 주어진다. 두 사람은 카드를 임의의 순서로 섞은 후 숫자가 보이지 않게 일렬로 늘어  놓고 게임을 시작한다. 단, 게임 도중 카드의 순서를 바꿀 수는 없다.

A와 B 각각이 늘어놓은 카드를 뒤집어서 표시된 숫자를 확인하는 것을 한 라운드라고 한다. 게임은 첫 번째 놓인 카드부터 시작하여 순서대로 10번의 라운드로 진행된다. 각 라운드에서는 공개된 숫자가 더 큰 사람이 승자가 된다. 승자에게는 승점 3점이 주어지고 패자에게는 승점이 주어지지 않는다. 만약 공개된 두 숫자가 같아서 비기게 되면, A, B 모두에게 승점 1점이 주어진다. 

10번의 라운드가 모두 진행된 후, 총 승점이 큰 사람이 게임의 승자가 된다. 만약, A와 B의 총 승점이 같은 경우에는, 제일 마지막에 이긴 사람을 게임의 승자로 정한다. 그래도 승부가 나지 않는 경우는 모든 라운드에서 비기는 경우뿐이고 이 경우에 두 사람은 비겼다고 한다.

예를 들어, 다음 표에서 3번째 줄은 각 라운드의 승자를 표시하고 있다. 표에서 D는 무승부를 나타낸다. 이 경우에 A의 총 승점은 16점이고, B는 13점이어서, A가 게임의 승자가 된다. 

| 라운드 | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| A      | 4    | 5    | 6    | 7    | 0    | 1    | 2    | 3    | 9    | 8    |
| B      | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 0    |
| 승     | A    | A    | A    | A    | B    | B    | B    | B    | D    | A    |

아래 표의 경우에는 A와 B의 총 승점은 13점으로 같다. 마지막으로 승부가 난 라운드는 7번째 라운드이고, 이 라운드의 승자인 B가 게임의 승자가 된다. 

| 라운드 | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| A      | 9    | 1    | 7    | 2    | 6    | 3    | 0    | 4    | 8    | 5    |
| B      | 6    | 3    | 9    | 2    | 1    | 0    | 7    | 4    | 8    | 5    |
| 승     | A    | B    | B    | D    | A    | A    | B    | D    | D    | D    |

A와 B가 늘어놓은 카드의 숫자가 순서대로 주어질 때, 게임의 승자가 A인지 B인지, 또는 비겼는지 결정하는 프로그램을 작성하시오.

#### 예시 입력

```output
4 5 6 7 0 1 2 3 9 8
1 2 3 4 5 6 7 8 9 0

9 1 7 2 6 3 0 4 8 5
6 3 9 2 1 0 7 4 8 5

7 1 6 2 3 0 5 9 4 8
7 1 6 2 3 0 5 9 4 8
```

#### 예시 출력

```output
16 13
A

13 13
B

10 10
D
```

#### 제출

```python
# A리스트 쭉 받고 B리스트 쭉 받아서 저장. 인덱스로 라운드 접근

a = list(map(int,input().split()))
b = list(map(int,input().split()))
sc_a = []
sc_b = []

for rnd in range(10):
    if a[rnd] > b[rnd]:
        sc_a.append(3)
        sc_b.append(0)
    elif a[rnd] < b[rnd]:
        sc_a.append(0)
        sc_b.append(3)
    else:
        sc_a.append(1)
        sc_b.append(1)

print(sum(sc_a),sum(sc_b))

if sum(sc_a) > sum(sc_b):
    print('A')
elif sum(sc_a) < sum(sc_b):
    print('B')
else:
    for i in range(10):
        if sc_a[9-i] > sc_b[9-i]:
            answer = 'A'
            break
        elif sc_a[9-i] < sc_b[9-i]:
            answer = 'B'
            break
        else:
            answer = 'D'

    print(answer)
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 10798     | 세로읽기  |

#### 문제

아직 글을 모르는 영석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다. 

이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 영석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다. 다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 이런 식으로 다섯 개의 단어를 만든다. 아래 그림 1은 영석이가 칠판에 붙여 만든 단어들의 예이다. 

```
A A B C D D
a f z z 
0 9 1 2 1
a 8 E W g 6
P 5 h 3 k x
```

<그림 1>

한 줄의 단어는 글자들을 빈칸 없이 연속으로 나열해서 최대 15개의 글자들로 이루어진다. 또한 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다. 

심심해진 영석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다. 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다. 이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다. 위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다. 그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다. 

그림 1에서 영석이가 세로로 읽은 순서대로 글자들을 공백 없이 출력하면 다음과 같다:

Aa0aPAf985Bz1EhCz2W3D1gkD6x

칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.

#### 예시 입력

```output
ABCDE
abcde
01234
FGHIJ
fghij

AABCDD
afzz
09121
a8EWg6
P5h3kx
```

#### 예시 출력

```output
Aa0FfBb1GgCc2HhDd3IiEe4Jj

Aa0aPAf985Bz1EhCz2W3D1gkD6x
```

#### 제출

```python
# 세로로 글자 읽기
# 리스트에 담아서 인덱스 순으로 쭉 읽기
# 리스트 길이 넘어가면 무시되도록

lst_1 = list(map(str,input()))
lst_2 = list(map(str,input()))
lst_3 = list(map(str,input()))
lst_4 = list(map(str,input()))
lst_5 = list(map(str,input()))
for i in range(max(len(lst_1),len(lst_2),len(lst_3),len(lst_4),len(lst_5))):
    if i >= len(lst_1):
        pass
    else:
        print(lst_1[i],end='')
    if i >= len(lst_2):
        pass
    else:
        print(lst_2[i],end='')
    if i >= len(lst_3):
        pass
    else:
        print(lst_3[i],end='')
    if i >= len(lst_4):
        pass
    else:
        print(lst_4[i],end='')
    if i >= len(lst_5):
        pass
    else:
        print(lst_5[i],end='')
```

 

---



| 문제 번호 | 문제 이름               |
| --------- | ----------------------- |
| 23825     | SASA 모형을 만들어 보자 |

#### 문제

당신은 SASA 연못에서 알파벳 S 모양의 블록 N$N$개와 알파벳 A 모양의 블록 M$M$개를 건졌다. 태영이는 연못에서 건진 블록을 이용해 학교에 전시할 SASA 모형을 최대한 많이 만들려고 한다.

SASA 모형 1$1$개를 만들기 위해서는, 알파벳 S 모양의 블록 2$2$개와 알파벳 A 모양의 블록 2$2$개가 필요하다. 태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 구하라.

#### 예시 입력

```output
4 5
```

#### 예시 출력

```output
2
```

#### 제출

```python
n, m = map(int, input().split())
print(min(n//2,m//2))
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 5622      | 다이얼    |

#### 문제

상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.

![img](https://upload.acmicpc.net/9c88dd24-3a4c-4a09-bc50-e6496958214d/-/preview/)

전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

#### 예시 입력

```output
WA

UNUCIC
```

#### 예시 출력

```output
13

36
```

#### 제출

```python
num = input()
cnt = 0
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for text in num:
    if alpha.index(text) < 3:
        cnt += 3
    elif alpha.index(text) < 6:
        cnt += 4
    elif alpha.index(text) < 9:
        cnt += 5
    elif alpha.index(text) < 12:
        cnt += 6
    elif alpha.index(text) < 15:
        cnt += 7
    elif alpha.index(text) < 19:
        cnt += 8
    elif alpha.index(text) < 22:
        cnt += 9
    elif alpha.index(text) < 26:
        cnt += 10
print(cnt)
```

 

---



| 문제 번호 | 문제 이름      |
| --------- | -------------- |
| 1292      | 쉽게 푸는 문제 |

#### 문제

동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.

이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

#### 예시 입력

```output
3 7
```

#### 예시 출력

```output
15
```

#### 제출

```python
a,b = map(int,input().split())
 
arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
 
print(sum(arr[a:b+1]))
```

 

---



| 문제 번호 | 문제 이름   |
| --------- | ----------- |
| 1357      | 뒤집힌 덧셈 |

#### 문제

어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.

두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

#### 예시 입력

```output
123 100

111 111

5 5

1000 1

456 789
```

#### 예시 출력

```output
223

222

1

2

1461
```

#### 제출

```python
x, y = input().split()
s = int(x[::-1].lstrip('0')) + int(y[::-1].lstrip('0'))
print(str(s)[::-1].lstrip('0'))
```

 

---



| 문제 번호 | 문제 이름   |
| --------- | ----------- |
| 10816     | 숫자 카드 2 |

#### 문제

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

#### 예시 입력

```output
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
```

#### 예시 출력

```output
3 0 0 1 2 0 0 2
```

#### 제출

```python
# 상근이 카드 리스트 입력
# 수자 딕셔너리 입력
# 하나씩 비교하여 카운트

n = int(input())
card_lst = list(map(int,input().split()))
m = int(input())
num_dic = list(map(int,input().split()))

for n in num_dic:
    print(card_lst.count(n), end=' ')
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 7785      |           |

#### 문제

상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.

각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.

상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.

#### 예시 입력

```output
4
Baha enter
Askar enter
Baha leave
Artem enter
```

#### 예시 출력

```output
Askar
Artem
```

#### 제출

```python
# 사람 이름을 받음, 상태를 받음
# leave는 -1 enter = +1 로 하고 1이상이면 안에 있다.
# 이름 리스트, 상태 리스트 각각 만들고 인덱스로 접근하여 통합
# for 상태가 1이상이면 인덱스 반환하여 그 사람의 이름 리스트에 따로 추가
# sorted하여 프린트

from unicodedata import name


t = int(input())
name_dic = dict()
ent_lst = []
for i in range(t):
    k, v = input().split()
    name_dic[k] = v
for key in name_dic:
    if name_dic[key] == 'enter':
        ent_lst.append(key)
ent_lst.sort(reverse=True)
for people in ent_lst:
    print(people)
```

 

---



| 문제 번호 | 문제 이름  |
| --------- | ---------- |
| 1302      | 베스트셀러 |

#### 문제

김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.

오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

#### 예시 입력

```output
5
top
top
top
top
kimtop

9
table
chair
table
table
lamp
door
lamp
table
chair

6
a
a
a
b
b
b

8
icecream
peanuts
peanuts
chocolate
candy
chocolate
icecream
apple

1
soul
```

#### 예시 출력

```output
top

table

a

chocolate

soul
```

#### 제출

```python
# 가장 많이 팔린 책
# 중복되면 사전상 가장 앞에 이름
# 최빈값? .mode
# 딕셔너리로 이름, 횟수 저장하고 값이 더 큰 경우에만 best 변수에 키 이름 저장

n = int(input())
sell_dic = dict()
for i in range(n):
    book = input()
    if book in sell_dic:
        sell_dic[book] += 1
    else:
        sell_dic[book] = 1
cnt = 0
best_lst = []
for key in sell_dic:
    if sell_dic[key] > cnt:
        best = key
        cnt = sell_dic[key]
for key in sell_dic:
    if sell_dic[key] == cnt:
        best_lst.append(key)
print(sorted(best_lst)[0])
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 1764      | 듣보잡    |

#### 문제

김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

#### 예시 입력

```output
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
```

#### 예시 출력

```output
2
baesangwook
ohhenrie
```

#### 제출

```python
# set으로 풀어보자
h,s = map(int,input().split())

hear = set()
saw = set()

for i in range(h):
    hear.add(input())
for i in range(s):
    saw.add(input())
hns = hear&saw
hns = sorted(hns) 
print(len(hns), *hns, sep='\n')
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 11652     | 카드      |

#### 문제

준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.

준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

#### 예시 입력

```output
5
1
2
1
2
1

6
1
2
1
2
1
2
```

#### 예시 출력

```output
1

1
```

#### 제출

```python
# # 가장 많이 팔린 책
# # 책 문제와 같은 유형 이름만 바꾸어 준다


n = int(input())
card_dic = dict()
for i in range(n):
    card_num = input()
    if card_num in card_dic:
        card_dic[card_num] += 1
    else:
        card_dic[card_num] = 1

num_lst = []
v_max = max(card_dic.values())
for k in card_dic:
    if card_dic[k] == v_max:
        num_lst.append(int(k))

print(min(num_lst))
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 2161      | 카드1     |

#### 문제

N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 버린 카드들은 순서대로 1 3 2가 되고, 남는 카드는 4가 된다.

N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.

#### 예시 입력

```output
7
```

#### 예시 출력

```output
1 3 5 7 4 2 6
```

#### 제출

```python
n = int(input())
queue = list(range(1,n+1))

while len(queue) > 1:
    print(queue.pop(0), end=' ')
    queue.append(queue.pop(0))

print(queue[0])
```

 

---



| 문제 번호 | 문제 이름              |
| --------- | ---------------------- |
| 23253     | 자료구조는 정말 최고야 |

#### 문제

N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 버린 카드들은 순서대로 1 3 2가 되고, 남는 카드는 4가 된다.

N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.

#### 예시 입력

```output
7
```

#### 예시 출력

```output
1 3 5 7 4 2 6
```

#### 제출

```python
n = int(input())
queue = list(range(1,n+1))

while len(queue) > 1:
    print(queue.pop(0), end=' ')
    queue.append(queue.pop(0))

print(queue[0])
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 9012      | 괄호      |

#### 문제

괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

#### 예시 입력

```output
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

3
((
))
())(()
```

#### 예시 출력

```output
NO
NO
YES
NO
YES
NO

NO
NO
NO
```

#### 제출

```python
n = int(input())
for _ in range(n):
    text = input()
    answer = 'YES'
    cnt = 0
    for i in text:
        if i == '(':
            cnt += 1
            # print(cnt)
        else:
            cnt -= 1
            # print(cnt)
        if cnt == -1:
            answer = 'NO'
            break
    if cnt != 0:
        answer = 'NO'
    print(answer)
```

 

---



| 문제 번호 | 문제 이름         |
| --------- | ----------------- |
| 2902      | KMP는 왜 KMP일까? |

#### 문제

KMP 알고리즘이 KMP인 이유는 이를 만든 사람의 성이 Knuth, Morris, Prett이기 때문이다. 이렇게 알고리즘에는 발견한 사람의 성을 따서 이름을 붙이는 경우가 많다.

또 다른 예로, 유명한 비대칭 암호화 알고리즘 RSA는 이를 만든 사람의 이름이 Rivest, Shamir, Adleman이다.

사람들은 이렇게 사람 성이 들어간 알고리즘을 두 가지 형태로 부른다.

- 첫 번째는 성을 모두 쓰고, 이를 하이픈(-)으로 이어 붙인 것이다. 예를 들면, Knuth-Morris-Pratt이다. 이것을 긴 형태라고 부른다.
- 두 번째로 짧은 형태는 만든 사람의 성의 첫 글자만 따서 부르는 것이다. 예를 들면, KMP이다.

동혁이는 매일매일 자신이 한 일을 모두 메모장에 적어놓는다. 잠을 자기 전에, 오늘 하루 무엇을 했는지 되새겨 보는 것으로 하루를 마감한다.

하루는 이 메모를 보던 중, 지금까지 긴 형태와 짧은 형태를 섞어서 적어 놓은 것을 발견했다.

이렇게 긴 형태로 하루 일을 기록하다가는 메모장 가격이 부담되어 파산될 것이 뻔하기 때문에, 앞으로는 짧은 형태로 기록하려고 한다.

긴 형태의 알고리즘 이름이 주어졌을 때, 이를 짧은 형태로 바꾸어 출력하는 프로그램을 작성하시오.

#### 예시 입력

```output
Knuth-Morris-Pratt

Mirko-Slavko

Pasko-Patak
```

#### 예시 출력

```output
KMP

MS

PP
```

#### 제출

```python
text_lst = list(map(str,input().split('-')))

for i in range(len(text_lst)):
    print(text_lst[i][0],end='')
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 14720     | 우유 축제 |

#### 문제

영학이는 딸기우유, 초코우유, 바나나우유를 좋아한다.

입맛이 매우 까다로운 영학이는 자신만의 우유를 마시는 규칙이 있다.

1. 맨 처음에는 딸기우유를 한 팩 마신다.
2. 딸기우유를 한 팩 마신 후에는 초코우유를 한 팩 마신다.
3. 초코우유를 한 팩 마신 후에는 바나나우유를 한 팩 마신다.
4. 바나나우유를 한 팩 마신 후에는 딸기우유를 한 팩 마신다. 

영학이는 우유 축제가 열리고 있는 우유거리에 왔다. 우유 거리에는 우유 가게들이 일렬로 늘어서 있다.

영학이는 우유 거리의 시작부터 끝까지 걸으면서 우유를 사먹고자 한다.

각각의 우유 가게는 딸기, 초코, 바나나 중 한 종류의 우유만을 취급한다.

각각의 우유 가게 앞에서, 영학이는 우유를 사마시거나, 사마시지 않는다.

우유거리에는 사람이 많기 때문에 한 번 지나친 우유 가게에는 다시 갈 수 없다.

영학이가 마실 수 있는 우유의 최대 개수를 구하여라.

#### 예시 입력

```output
7
0 1 2 0 1 2 0
```

#### 예시 출력

```output
7
```

#### 제출

```python
from collections import deque

n = int(input())
store = list(map(str,input().split()))
milk = deque(map(str,range(3)))
cnt = 0
for idx in range(n):
    if store[idx] == milk[0]:
        cnt += 1
        milk.append(milk.popleft())
print(cnt)
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 1076      | 저항      |

#### 문제

전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다. 처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다. 저항의 값은 다음 표를 이용해서 구한다.

| 색     | 값   | 곱            |
| :----- | :--- | :------------ |
| black  | 0    | 1             |
| brown  | 1    | 10            |
| red    | 2    | 100           |
| orange | 3    | 1,000         |
| yellow | 4    | 10,000        |
| green  | 5    | 100,000       |
| blue   | 6    | 1,000,000     |
| violet | 7    | 10,000,000    |
| grey   | 8    | 100,000,000   |
| white  | 9    | 1,000,000,000 |

예를 들어, 저항의 색이 yellow, violet, red였다면 저항의 값은 4,700이 된다.

#### 예시 입력

```output
yellow
violet
red

orange
red
blue

white
white
white
```

#### 예시 출력

```output
4700

32000000

99000000000
```

#### 제출

```python
color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
c_1 = input()
c_2 = input()
c_3 = input()

for idx in range(10):
    if color[idx] == c_1:
        n_1 = idx
    if color[idx] == c_2:
        n_2 = idx
    if color[idx] == c_3:
        n_3 = 10**idx
ohm = int(str(n_1)+str(n_2))*n_3
print(ohm)
```

 

---



| 문제 번호 | 문제 이름       |
| --------- | --------------- |
| 20001     | 고무오리 디버깅 |

#### 문제

백준 문제 풀이에 힘들어하는 수진이를 위해 민우는 문제해결에 도움이 되는 고무오리를 준비했다. 민우가 준비한 고무오리는 신비한 능력이 존재하는데, 최근에 풀던 백준 문제를 해결해주는 능력이다. 신비한 고무오리와 함께 수진이의 백준 풀이를 도와주자!

고무오리의 사용법은 다음과 같다.

- "고무오리 디버깅 시작" 이라고 외친다
- 문제들을 풀기 시작한다
- 고무오리를 받으면 최근 풀던 문제를 해결한다
- "고무오리 디버깅 끝" 이라고 외치면 문제풀이를 종료한다.

하지만 고무오리에는 치명적인 문제가 있는데, 풀 문제가 없는데 사용한다면 고무오리는 벌칙으 로 두 문제를 추가한다는 점이다.

#### 예시 입력

```output
고무오리 디버깅 시작
문제
고무오리
문제
문제
고무오리
고무오리
고무오리 디버깅 끝

고무오리 디버깅 시작
고무오리
고무오리
고무오리
고무오리 디버깅 끝

고무오리 디버깅 시작
문제
문제
고무오리
고무오리
고무오리
문제
고무오리
문제
고무오리
고무오리
고무오리
고무오리 디버깅 끝

고무오리 디버깅 시작
고무오리
고무오리 디버깅 끝
```

#### 예시 출력

```output
고무오리야 사랑해

고무오리야 사랑해

고무오리야 사랑해

힝구
```

#### 제출

```python
start = input()
s = 0
while True:
    text = input()
    if text == '고무오리 디버깅 끝':
        break
    if text == '문제':
        s += 1
    elif text == '고무오리':
        s -= 1
    if s == -1:
        s = 2
if s == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')
```

 

---



| 문제 번호 | 문제 이름       |
| --------- | --------------- |
| 10546     | 배부른 마라토너 |

#### 문제

마라토너라면 국적과 나이를 불문하고 누구나 참가하고 싶어하는 백준 마라톤 대회가 열린다. 42.195km를 달리는 이 마라톤은 모두가 참가하고 싶어했던 만큼 매년 모두가 완주해왔다. 단, 한 명만 빼고! 

모두가 참가하고 싶어서 안달인데 이런 백준 마라톤 대회에 참가해 놓고 완주하지 못한 배부른 참가자 한 명은 누굴까?

#### 예시 입력

```output
3
leo
kiki
eden
eden
kiki

5
marina
josipa
nikola
vinko
filipa
josipa
filipa
marina
nikola

4
mislav
stanko
mislav
ana
stanko
ana
mislav
```

#### 예시 출력

```output
leo

vinko

mislav
```

#### 제출

```python
import sys
input = sys.stdin.readline

names = dict()
n = int(input())
for _ in range(n):
    name = input()
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

for _ in range(n-1):
    name = input()
    names[name] -= 1

for key in names:
    if names[key] > 0:
        print(key)
        
# from collections import deque
# import sys
# input = sys.stdin.readline

# names = deque()
# finish = []
# n = int(input())
# for _ in range(n):
#     names.append(input())
# for _ in range(n-1):
#     finish.append(input())
# while len(names) > 1:
#     if names[0] == finish[-1]:
#         names.popleft()
#         finish.pop()
#     else:
#         names.append(names.popleft())
# print(*names)
```

 

---



| 문제 번호 | 문제 이름   |
| --------- | ----------- |
| 1269      | 대칭 차집합 |

#### 문제

자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오. 두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

예를 들어, A = { 1, 2, 4 } 이고, B = { 2, 3, 4, 5, 6 } 라고 할 때, A-B = { 1 } 이고, B-A = { 3, 5, 6 } 이므로, 대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.

#### 예시 입력

```output
3 5
1 2 4
2 3 4 5 6
```

#### 예시 출력

```output
4
```

#### 제출

```python
a, b = map(int,input().split())


a_lst = set(map(int,input().split()))
b_lst = set(map(int,input().split()))

print(len(a_lst ^ b_lst))
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 11286     | 절댓값 힙 |

#### 문제

절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

1. 배열에 정수 x (x ≠ 0)를 넣는다.
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

프로그램은 처음에 비어있는 배열에서 시작하게 된다.

#### 예시 입력

```output
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
```

#### 예시 출력

```output
-1
1
0
-1
-1
1
1
-2
2
0
```

#### 제출

```python
import sys
input = sys.stdin.readline
# sys.stdin = open('11286.txt')
import heapq

heap = []

n = int(input())
for _ in range(n):
    num = int(input())
    if num < 0:
        heapq.heappush(heap,[abs(num),-1])
    elif num > 0:
        heapq.heappush(heap,[abs(num),1])
    elif num == 0:
        if len(heap) == 0:
            print(0)
        else:
            number = heapq.heappop(heap)
            print(number[0]*number[1])
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 5063      | TGN       |

#### 문제

상근이는 TGN사의 사장이다. TGN은 Teenager Game Network의 약자 같지만, 사실 Temporary Group Name의 약자이다.

이 회사는 청소년을 위한 앱을 만드는 회사이다. 일년에 걸친 개발기간 끝에 드디어 앱을 완성했고, 이제 팔기만 하면 된다.

상근이는 데이트를 인간의 두뇌로 이해할 수 없을 정도로 많이 한다. 따라서 엄청난 데이트 비용이 필요하다. 상근이는 광고를 적절히 해서 수익을 최대한 올리려고 한다.

어느 날 하늘을 바라보던 상근이는 시리우스의 기운을 받게 되었고, 광고 효과를 예측하는 능력을 갖게 되었다.

광고 효과가 주어졌을 때, 광고를 해야할지 말아야할지 결정하는 프로그램을 작성하시오.

#### 예시 입력

```output
3
0 100 70
100 130 30
-100 -70 40
```

#### 예시 출력

```output
advertise
does not matter
do not advertise
```

#### 제출

```python
n = int(input())

for _ in range(n):
    r, e, c = map(int,input().split())
    if r > e-c:
        print('do not advertise')
    elif r == e-c:
        print('does not matter')
    else:
        print('advertise')
```

 

---



| 문제 번호 | 문제 이름   |
| --------- | ----------- |
| 2750      | 수 정렬하기 |

#### 문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#### 예시 입력

```output
5
5
2
3
4
1
```

#### 예시 출력

```output
1
2
3
4
5
```

#### 제출

```python
import heapq

n = int(input())

heap = []
for _ in range(n):
    num = int(input())
    heapq.heappush(heap,num)
for _ in range(n):
    print(heapq.heappop(heap))
```

 

---



| 문제 번호 | 문제 이름     |
| --------- | ------------- |
| 4949      | 균형잡힌 세상 |

#### 문제

세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

- 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
- 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
- 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
- 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
- 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.

정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

#### 예시 입력

```output
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
```

#### 예시 출력

```output
yes
yes
no
no
no
yes
yes
```

#### 제출

```python
# while True:
#     big, small = 0, 0
#     text_line = input()
#     answer = 'no'
#     if text_line == '.':
#         break
#     for text in text_line:
#         print(text)
#         if text == '(':
#             small += 1
#         elif text == ')':
#             small -= 1
#         elif text == '[':
#             big += 1
#         elif text == ']':
#             big -= 1
#         if small < 0 or big < 0:
#             break
#     if small == 0 and big == 0:
#         answer = 'yes'
#     print(answer)
#     break

while True:
    gual = []
    text_line = input()
    if text_line == '.':
        break
    for text in text_line:
        if text in '()[]':
            gual.append(text)
    string = ''.join(gual)
    while '()' in string or '[]' in string:
        string = ''.join(gual)
        if '()' in string:
            idx = string.index('()')
            gual.pop(idx)
            gual.pop(idx)
            string = ''.join(gual)
        if '[]' in string:
            idx = string.index('[]')
            gual.pop(idx)
            gual.pop(idx)
    if len(gual) != 0:
        print('no')
    else:
        print('yes')
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 2776      | 암기왕    |

#### 문제

연종이는 엄청난 기억력을 가지고 있다. 그래서 하루 동안 본 정수들을 모두 기억 할 수 있다. 하지만 이를 믿을 수 없는 동규는 그의 기억력을 시험해 보기로 한다. 동규는 연종을 따라 다니며, 연종이 하루 동안 본 정수들을 모두 ‘수첩1’에 적어 놓았다. 그것을 바탕으로 그가 진짜 암기왕인지 알아보기 위해, 동규는 연종에게 M개의 질문을 던졌다. 질문의 내용은 “X라는 정수를 오늘 본 적이 있는가?” 이다. 연종은 막힘없이 모두 대답을 했고, 동규는 연종이 봤다고 주장하는 수 들을 ‘수첩2’에 적어 두었다. 집에 돌아온 동규는 답이 맞는지 확인하려 하지만, 연종을 따라다니느라 너무 힘들어서 여러분에게 도움을 요청했다. 동규를 도와주기 위해 ‘수첩2’에 적혀있는 순서대로, 각각의 수에 대하여, ‘수첩1’에 있으면 1을, 없으면 0을 출력하는 프로그램을 작성해보자.

#### 예시 입력

```output
1
5
4 1 5 2 3
5
1 3 7 9 5
```

#### 예시 출력

```output
1
1
0
0
1
```

#### 제출

```python
n = int(input())
for _ in range(n):
    a = int(input())
    a_set = set(map(int,input().split()))
    b = int(input())
    b_lst = list(map(int,input().split()))

    for num in b_lst:
        if num in a_set:
            print(1)
        else:
            print(0)
```

 

---



| 문제 번호 | 문제 이름          |
| --------- | ------------------ |
| 25192     | 인사성 밝은 곰곰이 |

#### 문제

알고리즘 입문방 오픈 채팅방에서는 새로운 분들이 입장을 할 때마다 곰곰티콘을 사용해 인사를 한다. 이를 본 문자열 킬러 임스는 채팅방의 기록을 수집해 그 중 곰곰티콘이 사용된 횟수를 구해 보기로 했다.

`ENTER`는 새로운 사람이 채팅방에 입장했음을 나타낸다. 그 외는 채팅을 입력한 유저의 닉네임을 나타낸다. 닉네임은 숫자 또는 영문 대소문자로 구성되어 있다.

새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다. 그 외의 기록은 곰곰티콘을 쓰지 않은 평범한 채팅 기록이다.

채팅 기록 중 곰곰티콘이 사용된 횟수를 구해보자!

#### 예시 입력

```output
9
ENTER
pjshwa
chansol
chogahui05
lms0806
pichulia
r4pidstart
swoon
tony9402

7
ENTER
pjshwa
chansol
chogahui05
ENTER
pjshwa
chansol

3
ENTER
lms0806
lms0806
```

#### 예시 출력

```output
8

5

1
```

#### 제출

```python
n = int(input())

gom_set = set()
cnt_lst = []

for _ in range(n):
    text = input()
    if text == 'ENTER':
        cnt_lst.append(len(gom_set))
        gom_set = set()
    else:
        gom_set.add(text)
cnt_lst.append(len(gom_set))

print(sum(cnt_lst))
```

 

---



| 문제 번호 | 문제 이름    |
| --------- | ------------ |
| 10989     | 수 정렬하기3 |

#### 문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#### 예시 입력

```output
10
5
2
3
1
4
2
3
5
1
7
```

#### 예시 출력

```output
1
1
2
2
3
3
4
5
5
7
```

#### 제출

```python
import sys
input = sys.stdin.readline
N = int(input())

check_list = [0] * 10001

for i in range(N):
    input_num = int(input())
    
    check_list[input_num] = check_list[input_num] + 1
    
for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)
```

 



---



| 문제 번호 | 문제 이름    |
| --------- | ------------ |
| 2864      | 5와 6의 차이 |

#### 문제

상근이는 2863번에서 표를 너무 열심히 돌린 나머지 5와 6을 헷갈리기 시작했다.

상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.

두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.

#### 예시 입력

```output
11 25

1430 4862

16796 58786
```

#### 예시 출력

```output
36 37

6282 6292

74580 85582
```

#### 제출

```python
num_1, num_2 = input().split()
matrix = [list(num_1),list(num_2)]

small, big = 0, 0
for n in range(2):
    for idx in range(len(matrix[n])):
        number = int(matrix[n][-idx-1])
        if number == 6:
            small += 5*10**idx
        else:
            small += number*10**idx
for n in range(2):
    for idx in range(len(matrix[n])):
        number = int(matrix[n][-idx-1])
        if number == 5:
            big += 6*10**idx
        else:
            big += number*10**idx
print(small, big)
```

 

---



| 문제 번호 | 문제 이름 |
| --------- | --------- |
| 15953     | 상금헌터  |

#### 문제

카카오 코드 페스티벌에서 빠질 수 없는 것은 바로 상금이다. 2017년에 개최된 제1회 코드 페스티벌에서는, 본선 진출자 100명 중 21명에게 아래와 같은 기준으로 상금을 부여하였다.

| 순위 | 상금    | 인원 |
| :--- | :------ | :--- |
| 1등  | 500만원 | 1명  |
| 2등  | 300만원 | 2명  |
| 3등  | 200만원 | 3명  |
| 4등  | 50만원  | 4명  |
| 5등  | 30만원  | 5명  |
| 6등  | 10만원  | 6명  |

2018년에 개최될 제2회 코드 페스티벌에서는 상금의 규모가 확대되어, 본선 진출자 64명 중 31명에게 아래와 같은 기준으로 상금을 부여할 예정이다.

| 순위 | 상금    | 인원 |
| :--- | :------ | :--- |
| 1등  | 512만원 | 1명  |
| 2등  | 256만원 | 2명  |
| 3등  | 128만원 | 4명  |
| 4등  | 64만원  | 8명  |
| 5등  | 32만원  | 16명 |

![img](https://upload.acmicpc.net/2ff64533-7387-4294-8dce-03ba3d35b7d4/-/preview/)

제이지는 자신이 코드 페스티벌에 출전하여 받을 수 있을 상금이 얼마인지 궁금해졌다. 그는 자신이 두 번의 코드 페스티벌 본선 대회에서 얻을 수 있을 총 상금이 얼마인지 알아보기 위해, 상상력을 발휘하여 아래와 같은 가정을 하였다.

- 제1회 코드 페스티벌 본선에 진출하여 *a*등(1 ≤ *a* ≤ 100)등을 하였다. 단, 진출하지 못했다면 *a* = 0으로 둔다.
- 제2회 코드 페스티벌 본선에 진출하여 *b*등(1 ≤ *b* ≤ 64)등을 할 것이다. 단, 진출하지 못했다면 *b* = 0으로 둔다.

제이지는 이러한 가정에 따라, 자신이 받을 수 있는 총 상금이 얼마인지를 알고 싶어한다.

#### 예시 입력

```output
6
8 4
13 19
8 10
18 18
8 25
13 16
```

#### 예시 출력

```output
1780000
620000
1140000
420000
820000
620000
```

#### 제출

```python
a_test = [0] + [500]*1 + [300]*2 + [200]*3 + [50]*4 + [30]*5 + [10]*6 + [0]*(100-21)
b_test = [0] + [512]*1 + [256]*2 + [128]*4 + [64]*8 + [32]*16 + [0]*(64-31)

n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    print((a_test[a] + b_test[b])*10000)
```

 

---



| 문제 번호 | 문제 이름            |
| --------- | -------------------- |
| 24523     | 내 뒤에 나와 다른 수 |

#### 문제

길이가 N인 수열 A1 A2 ⋯ AN 이 주어진다. 1 ≤ i ≤ N 인 정수 i 마다 i < j ≤ N 이고 Ai ≠ Aj인 정수 j$ 중 최솟값을 출력하라. 만약 이러한 j가 없다면 −1 을 출력하라.

#### 예시 입력

```output
6
3 3 1 1 4 4
```

#### 예시 출력

```output
3 3 5 5 -1 -1
```

#### 제출

```python
num_1, num_2 = input().split()
matrix = [list(num_1),list(num_2)]

small, big = 0, 0
for n in range(2):
    for idx in range(len(matrix[n])):
        number = int(matrix[n][-idx-1])
        if number == 6:
            small += 5*10**idx
        else:
            small += number*10**idx
for n in range(2):
    for idx in range(len(matrix[n])):
        number = int(matrix[n][-idx-1])
        if number == 5:
            big += 6*10**idx
        else:
            big += number*10**idx
print(small, big)
```

 
