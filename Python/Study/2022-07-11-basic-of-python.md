# Python 기초



## 컴퓨터 프로그래밍 언어

- **컴퓨터** : Calculation + Remember

- **프로그래밍** : 명령어의 모으머

- **언어** : `자신의 생각`을 전달하기 위해 `문법적`으로 맞는 말의 집합

  > '알잘딱깔센', '만반잘부' 등 약속되지 않은 언어는 알 수가 없다.

- 선언적 지식 : 사실에 대한 내용
- 명령적 지식 : 내가 무슨 명령을 할력호 했는지 항상 생각하기



## 파이썬 개발 환경

### Python 특징

- Easy to learn : 문법이 간단하며 엄격하지 않음

- Expressive Language : 같은 작업도 더 간결하게 작성

- Cross Platform Language : 다양한 운영체제에서 실행 가능

- Interpreter Language : 컴파일 과정 없이 바로 실행 가능

- Object Oriented Programming : 객체 지향 언어이며, 모든 것이 객체로 구현

  > 객체 : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것 (somethings)

### Python 개발환경

- IDLE(Intergrated Development and Learning Environment)

  > 내장 프로그램 설치 시 기본적으로 설치 => 대화형 모드 동작 => 디버깅 및 코드 편집 어려움

- IDE, Text Editor 등에서 작성한 파이썬 스크립트 파일을 직접 실행

  > IDE : Pycharm, Text Editor : Visual Studio Code 등



## 기초 문법

### 코드 스타일 가이드

- 코드를 어떻게 작성할지에 대한 가이드라인

  > 파이썬에서 제안하는 스타일 가이드
  >
  > PEP8 : https://www.python.org/dev/peps/pep-0008/
  >
  > 기업, 오픈소스 등에서 사용되는 스타일 가이드
  >
  > Google Style Guide : https://google.github.io/styleguide/pyguide.html

  > #### 들여쓰기
  >
  > Space Sensitive
  >
  > 문장을 구분할 때, 들여쓰기 사용
  >
  > 원칙적으로는 공백사용 권장

### 변수(Variable)

- 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

- 변수는 할당 연산자 (=)를 통해 값을 할당

- 변수에 할당된 값의 type, id 값 존재

  ```python
  x = 'hi'
  type(x)
  # str
  id(x)
  # 4645387184
  ```

	#### 예제
	
	```python
	i = 5
	j = 3
	s = '파이썬'
	
	i + j     # 8
	i - j     # 2
	j = -2
	i*j       # -10  -> j가 새로 할당되어서 변수 값 변화
	
	'안녕' + s    # 안녕 파이썬
	s*3           # 파이썬파이썬파이썬
	s = 'Python'
	s + 'is fun'     # Python is fun
	```
	
	#### 변수 할당
	
	```python
	x = y = 1004   # x = 1004,  y = 1004
	x,y = 1, 4     # x = 1,   y = 4
	```
	
	#### 예제
	
	```python
	# 각 변수의 값을 서로 바꿔서 저장하는 코드 작성하시오
	x, y = 10, 20
	
	y, x = x, y  # Pythonic한 방법!
	```



### 식별자(Identifiers)

- 파이썬 객첵를 식별하는데 사용하는 이름

- 규칙

  - 영문 알파벳, 언더스코어(_), 숫자로 구성

  - 첫 글자 숫자 불가능

  - 대소문자 구별

  - 이미 할당되어 있는 예약어는 사용 불가

    > False, True, while 등

    ``` python
    # 예약어 확인
    import keyword
    print(keyword.kwlist)
    ```

  - 내장 함수나 모듈 등의 이름으로도 불가능

    ```python
    print = 5
    ```



### 사용자 입력

- 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수

  ```python
  name = input()    # 4 입력    => 입력 받은 값은 항상 문자열!!!! -> 데이터 형 변환 하면 숫자 정수형, 실수형 변경 가능
  print(name)       # 4 출력
  
  name_int = int(input()) # 입력값 정수형 변환
  name_float = float(input()) # 입력값 실수형 변환
  ```

### 주석

- 코드에 대한 설명

  > \# 다음에 주석 내용 입력
  >
  > 전체 주석 하고 싶으면 범위 선택 후 'ctrl + /'





## 기본 자료형

> ## Data type
>
> - String
> - Boolean
> - Numeric
>   - Int
>   - Float
>   - Complex
> - None

### None

- 파이썬 자료형 중 하나
- 일반적으로 반환 값이 없는 함수에서 사용하기도 함

### Boolean

- Ture / Flase 값을 가진 타입은 bool

- bool() 함수

  > 특정 함수가 참인지 것짓인지 검증

  ```python
  bool(0)  # False
  bool(1)  # True
  bool(-1) # False
  bool('') # False
  bool([]) # Flase
  bool([1,2,3]) # True
  ```

- 논리 연산자

  > 논리식을 판단하여 참과 거짓을 반환함

  | 연산자  |              내용              |
  | :-----: | :----------------------------: |
  | A and B |    A와 B 모두 True시, True     |
  | A or B  |   A와 B 모두 Flase시, False    |
  |   Not   | True를 Flase로, False를 True로 |

- 연산자 예제

  ```python
  num = 100
  num >= 100 and num % 3 == 1
  # True
  ```

### Numeric Type

- Int(정수형)

  - 모든 정수의 타입은 int

  - 다른 언어처럼 long 타입 존재 안한다. 모든 정수는 int

    > 오버 플로우가 발생하지 않는다.

- Float(실수형)

  - 정수가 아닌 모든 실수는 float

  - 부동 소수점

    - 실수를 컴퓨터가 표현하는 방법 - 2진수로 숫자를 표현

      > 이 과정에서 floating point rounding error가 발생하여 예상치 못한 결과 발생

      ```python
      # 아래는 참일까 거짓일까?
      3.14 - 3.02 == 0.12
      # 0.1200000000000000001  => 에러 발생
      ```

      > 비교를 위해 실수를 뺄 때는 다음과 같이

      ```python
      # 1. 임의의 작은 수
      abs(a - b) <= 1e-10
      
      # 2. math 모듈 활용
      math.isclose(a,b)
      
      # 두 값의 차이가 매우 작은 수보다 작으면 같다고 보자!
      ```

- Complex(복소수)

  - 실수부와 허수부로 구성된 복소수는 모두 complex 타입

    ```python
    a = 3 + 4j
    type(a)
    # class complex
    a.real
    # 3.0
    a.imag
    # 4.0
    ```

- 산술 연산자

  | 연산자 |   내용   |
  | :----: | :------: |
  |   +    |   덧셈   |
  |   -    |   뺄셈   |
  |   *    |   곱셈   |
  |   /    |  나눗셈  |
  |   //   |    몫    |
  |   %    |  나머지  |
  |   **   | 거듭제곱 |

- 복합 연산자

  | 연산자  |    내용    |
  | :-----: | :--------: |
  | a += b  | a = a + b  |
  | a -= b  | a = a - b  |
  | a *= b  | a = a * b  |
  | a /= b  | a = a / b  |
  | a //= b | a = a // b |
  | a %= b  | a = a % b  |
  | a **= b | a = a ** b |

- 비교 연산자

  | 연산자 |            내용             |
  | :----: | :-------------------------: |
  |   <    |            미만             |
  |   <=   |            이하             |
  |   >    |            초과             |
  |   >=   |            이상             |
  |   ==   |            같음             |
  |   !=   |          같지않음           |
  |   is   |       객체 아이덴티티       |
  | is not | 객체 아이덴티티가 아닌 경우 |



### String Type

- 모든 문자는 str 타입

- 문자열은 작은 따옴표(')나 큰 따옴표 (") 활용하여 표기

  ```python
  print('hello')
  print("hello")
  
  # 중첩 따옴표
  print('그는 "안녕하세요"라고 말했다')
  print("그는 '안녕하세요'라고 말했다")
  
  # 삼중 따옴표
  print('''문자열 안에 '작은 따옴표'또는 "큰따옴표" 모두 사용 가능''')
  ```

- 인덱싱

  | 변수s |  a   |  b   |  c   |  d   |  e   |  f   |  g   |  h   |  i   |
  | :---: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
  | index |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   |
  | index |  -9  |  -8  |  -7  |  -6  |  -5  |  -4  |  -3  |  -2  |  -1  |

  ```python
  s[4] = 'e'
  
  # 슬라이싱
  s[2:5] = 'cde'
  s[2:5:2] = 'ce'
  s[5:2:-1] = 'fed'     # s[2:5:-1] 은 에러 난다!
  s[:3] = 'abc'
  s[5:] = 'fghi'
  s[::] = 'abcdefghi'
  s[::-1] = 'ihgfedcba'
  ```

- 기타

  - 결합

    ```python
    'hello, ' + 'python'
    # hello, python
    ```

  - 반복

    ```python
    'hi!'*3
    # hi!hi!hi!
    ```

  - 포함

    ```python
    'a' in 'apple'
    # True
    'b' in 'apple'
    # False
    ```

- Escape Sequence

  | 예약문자 |   내용(의미)    |
  | :------: | :-------------: |
  |    \n    |     줄 바꿈     |
  |    \t    |       탭        |
  |    \r    |   캐리지리턴    |
  |    \0    |    널(Null)     |
  |   \\\\   |       \\        |
  |   \\\'   | 단일인용부호(') |
  |   \\\"   | 이중인용부호(") |

- String Interpolation

  - 문자열을 변수를 활용하여 만드는 법

    - % formatting

      ```python
      name = 'Kim'
      score = 4.5
      
      print('Hello, %s' % name)       # Hello, Kim
      print('내 성적은 %d' % score)    # 내 성적은 4
      print('내 성적은 %f' % score)    # 내 성적은 4.50000
      ```

    - f-string

      ```python
      name = 'Kim'
      score = 4.5
      
      print(f'Hello, {name}! 성적은 {score}')
      # Hello, Kim! 성적은 4.5
      ```

- 문자열 특징
  - Immutable (변경 가능함)
  - Iterable (반복 가능함)





### Typecasting

- 형 변환

  - 암시적 형 변환

    ```python
    True + 3      # 4
    
    3 + 5.0       # 8.0
    
    3 + 4j + 5    # 8 + 4j
    ```

  - 명시적 형 변환

    ```python
    '3' + 4       # Error
    int('3') + 4  # 7
    ```



### Container

- 여러 개의 값을 담을 수 있는 것으로, 서로 다른 자료형을 저장할 수 있음
- 컨테이너의 분류
  - 순서가 있는 데이터 ( 시퀀스 )
    - 문자열 : 문자들의 나열
    - 리스트 : 변경 가능한 것들의 나열
    - 튜플 : 변경 불가능한 값들의 나열
    - 레인지 : 숫자의 나열
  - 순서가 없는 데이터 ( 비시퀀스 )
    - 세트 : 유일한 값들의 모음
    - 딕셔너리 : 키-값들의 모음

#### 시퀀스형

- **리스트**의 정의

  - 변경 가능한 값들이 나열된 자료형

  - 리스트는 대괄호([]) 또는 list() 를 통해서 생성

    ```python
    # 생성
    my_list = []
    another_list = list()
    type(my_list)
    # <class 'list'>
    type(another_list)
    # <class 'list'>
    ```

  - 추가 / 삭제

    ```python
    # ~~~.append()    # 추가 하고자 하는 "값" 전달
    e = [1,2,3,4,5]
    e.append(10)
    e = [1,2,3,4,5,10]
    
    # ~~~.pop()        # 지우고자 하는 "인덱스" 전달
    e = [1,2,3,4,5]
    e.pop(0)
    e = [2,3,4,5,10]
    ```



- 튜플의 정의

  - 불변한 값들의 나열, 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음

  - 변경 불가능, 반복 가능

  - 소괄호로 형태 정의, 콤마로 요소 구분

  - 생성과 접근

    ```python
    # 값 접근
    a = (1, 2, 3, 1)
    a[1]
    
    # 값 변경 => 불가능
    a[1] = '3'
    ```

    

- 레인지

  - 숫자의 시퀀스를 나타내기 위해 사용

    - 기본형 : range (n)

      > 0부터 n-1 까지의 숫자 시퀀스

    - 범위 지정 : range(n,m)

      > n부터 m-1 까지의 숫자 시퀀스

    - 범위 및 스텝 지정

      > n부터 m-1 까지 s만큼 증가시키는 숫자 시퀀스

  - 변경 불가능, 반복 가능

  - 예시

    ```python
    range(4)               # range(0,4)
    
    list(range(4))         # [0, 1, 2, 3]
    
    type(range(4))         # <class 'range'>
    
    # 0부터 특정 숫자 까지
    list(range(3))          # [0, 1, 2]
    # 숫자의 범위
    list(range(1,5))        # [1, 2, 3, 4]
    # step 활용
    list(range(1, 5, 2))    # [1, 3]
    
    # 역순
    list(range(6, 1, -1))    # [6, 5, 4, 3, 2]
    
    list(range(6, 1, 1))     # []
    
    ```

    

#### 비시퀀스형

- 세트
  - 유일한 값들의 모음
  
  - 순서가 없고 중복된 값이 없음
  
  - 변경 가능하며, 반복 가능함
  
  - 생성
  
    ```python
    {1,2,3,2,1}
    # {1, 2, 3}   ---> 중복값 제거
    type({1, 2, 3})
    # class set
    {1, 2, 3}[1] #---> 순서가 없으므로 인덱스 사용시 에러
    ```
  
    

- 딕셔너리

  - 키-값 쌍으로 이루어진 모음

    - 키 : 불변 자료형만 가능(리스트, 딕셔너리 등은 불가능)
    - 값 : 어떠한 형태든 관계 없음

  - 키와 값은 **`:`**로 구분된다

  - 변경 가능하고 반복 가능

  - 생성

    ```python
    movie = {
        'title' : '설국열차',
        'genres' : ['SF', '액션', '드라마'],
        'time' : 126,
        'adult' : False,
    }
    
    movie['genres']
    # ['SF', '액션', '드라마']
    ```

  - 추가 및 변경

    ```python
    students = {'홍길동':100, '김철수':90}
    students['홍길동'] = 80
    # {'홍길동': 80, '김철수' : 90}
    students['박영희'] = 95
    # {'홍길동': 80, '김철수' : 90, '박영희' : 95}
    ```

  - 삭제

    ```python
    students.pop('홍길동')
    students
    # {'김철수' : 90, '박영희' : 95}
    ```

    
