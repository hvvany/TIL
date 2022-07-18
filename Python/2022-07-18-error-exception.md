

# Python Error / Error Exception

---

## 디버깅

- ### 디버깅 위치

  - brancehs

    > 모든 조건이 원하는대로 동작하는지

  - for loops

    > 반복문에 진입하는지, 원하는 횟수만큼 실행되는지

  - while loops

    > for loops 와 동일, 종료조건이 제대로 동작하는지

  - function

    > 함수 호출시, 함수 파라미터, 함수 결과



- ### 디버깅 방법

  > ### "코드의 상태를 신중하게 출력해가며 심사숙고하는 것보다
  >
  > ###  효과적인 디버깅 도구는 없습니다.”
  >
  >  —브라이언 커니핸, Unix for Beginners.

  - print함수 활용
  - 개발 환경에서 제공하는 기능 활용
  - Python tutor 활용 (단순 파이썬 코드인 경우)
  - 뇌컴파일, 눈디버깅



- ### 코드를 작성하다가

  - **에러 메시지가 발생하는 경우**
    * 해당 위치를 찾아 메시지를 해결

  - **로직 에러가 발생하는 경우**
    - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
    - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
    - 전체 코드를 살펴봄
    - 휴식을 가져봄
    - 누군가에게 설명해봄
    - ...



## 에러와 예외

- ### 문법 에러 (Syntax Error)

  ```python
  if else
  ```

  ```python
  File "<ipython-input-1-f8a097d0a685>", line 1
  if else ^
  SyntaxError: invalid syntax
  ```

  - EOL (End of Line)

  ```python
  print('hello
  # File "<ipython-input-6-2a5f5c6b1414>", line 1
  # print('hello
  # ^
  # SyntaxError: EOL while scanning string literal
  ```

  - EOF (End of File)

  ```python
  print(
  # File "<ipython-input-4-424fbb3a34c5>", line 1
  # print(
  # ^
  # SyntaxError: unexpected EOF while parsing
  ```

  - Invalid syntax

  ```python
  while
  # File "<ipython-input-7-ae84bbebe3ce>", line 1
  # while
  # ^
  # SyntaxError: invalid syntax
  ```

  - assign to literal

  ```python
  5 = 3
  # File "<ipython-input-28-9a762f2c796b>", line
  1
  # 5 = 3
  # ^
  # SyntaxError: cannot assign to literal
  ```



- ### 예외(Exception)

  - 문장이나 표현식이 문법적으로 올바르다 해도 에러 발생 가능
  - 실행 중에 감지되는 에러들을 예외라고 부른다

- ZeroDivisionError

  > 0으로 나누고자 할 때 발생

  ```python
  10/0
  # ---------------
  # ZeroDivisionError Traceback (most recent call last)
  # ----> 1 10/0
  # ZeroDivisionError: division by zero
  ```

- NameError

  > namespace 상에 이름이 없는 경우

  ```python
  print(name_error)
  # ---------------------------
  # NameError Traceback (most recent call last)
  # ----> 1 print(name_error)
  # NameError: name 'name_error' is not defined
  ```

- TypeError

  > 타입 불일치

  ```python
  1 + '1'
  # --------------
  # TypeError Traceback (most recent call last)
  # ----> 1 1 + '1'
  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
  round('3.5')
  # ---------------
  # TypeError Traceback (most recent call last)
  # ----> 1 round('3.5')
  # TypeError: type str doesn't define __round__ method
  ```

  > arguments 부족

  ```python
  divmod()
  # ------------
  # TypeError Traceback (most recent call last)
  # ----> 1 divmod()
  # TypeError: divmod expected 2 arguments, got 0
  import random
  random.sample()
  # ---------
  # TypeError Traceback (most recent call last)
  # 1 import random
  # ----> 2 random.sample()
  # TypeError: sample() missing 2 required positional arguments:
  'population' and 'k'
  ```

  > arguments 개수 초과

  ```python
  divmod(1, 2, 3)
  # ---------
  # TypeError Traceback (most recent call last)
  # ----> 1 divmod(1, 2, 3)
  # TypeError: divmod expected 2 arguments, got 3
  import random
  random.sample(range(3), 1, 2)
  # --------
  # TypeError Traceback (most recent call last)
  # 1 import random
  # ----> 2 random.sample(range(3), 1, 2)
  # TypeError: sample() takes 3 positional arguments but 4 were given
  ```

  

- ValueError

  > 타입은 올바르나 값이 적절하지 않거나 없는 경우

  ```python
  int('3.5')
  # ------
  # ValueError Traceback (most recent call last)
  # ----> 1 int('3.5')
  # ValueError: invalid literal for int() with base 10:
  '3.5'
  range(3).index(6)
  # ------
  # ValueError Traceback (most recent call last)
  # ----> 1 range(3).index(6)
  # ValueError: 6 is not in range
  ```

- IndexError

  ```python
  empty_list = []
  empty_list[2]
  # ------
  # IndexError Traceback (most recent call last)
  # 1 empty_list = []
  # ----> 2 empty_list[2]
  # IndexError: list index out of range
  ```

- KeyError

  ```python
  song = {'IU': '좋은날'}
  song['BTS']
  # ------
  # KeyError Traceback (most recent call last)
  # 1 song = {'IU': '좋은날'}
  # ----> 2 song['BTS']
  # KeyError: 'BTS'
  ```

- ModuleNotFoundError

  > 존재하지 않는 모듈을 import 하는 경우

  ```python
  import nonamed
  # ------
  # ModuleNotFoundError Traceback (most recent call last)
  # ----> 1 import nonamed
  # ModuleNotFoundError: No module named 'nonamed
  ```

- ImportError

  > Module은 있으나 존재하지않는 클래스/함수를 가져오는 경우

  ```python
  from random import samp
  # ------
  # ImportError Traceback (most recent call last)
  # ----> 1 from random import samp
  # ImportError: cannot import name 'samp' from 'random'
  ```

- IndentationError

  > Indentation이 적절하지 않는 경우

  ```python
  for i in range(3):
  print(i)
  # File "<ipython-input-56-78291925d94f>", line 2
  # print(i)
  # ^
  # IndentationError: expected an indented block
  ```

- KeyboardInterrupt

  > 임의로 프로그램을 종료하였을 때

  ```python
  while True:
  continue
  # ------
  # KeyboardInterrupt Traceback (most recent call last)
  # <ipython-input-55-6a65cf439648> in <module>
  # 1 while True:
  # ----> 2 continue
  # KeyboardInterrupt:
  ```

- ZeroDivisionError

  ```python
  10/0
  ```

- 파이썬 내장 예외

	```txt
  BaseException
   +-- SystemExit
   +-- KeyboardInterrupt
   +-- GeneratorExit
   +-- Exception
        +-- StopIteration
        +-- StopAsyncIteration
        +-- ArithmeticError
        |    +-- FloatingPointError
        |    +-- OverflowError
        |    +-- ZeroDivisionError
        +-- AssertionError
        +-- AttributeError
        +-- BufferError
        +-- EOFError
        +-- ImportError
        |    +-- ModuleNotFoundError
        +-- LookupError
        |    +-- IndexError
        |    +-- KeyError
        +-- MemoryError
        +-- NameError
        |    +-- UnboundLocalError
        +-- OSError
        |    +-- BlockingIOError
        |    +-- ChildProcessError
        |    +-- ConnectionError
        |    |    +-- BrokenPipeError
        |    |    +-- ConnectionAbortedError
        |    |    +-- ConnectionRefusedError
        |    |    +-- ConnectionResetError
        |    +-- FileExistsError
        |    +-- FileNotFoundError
        |    +-- InterruptedError
        |    +-- IsADirectoryError
        |    +-- NotADirectoryError
        |    +-- PermissionError
        |    +-- ProcessLookupError
        |    +-- TimeoutError
        +-- ReferenceError
        +-- RuntimeError
        |    +-- NotImplementedError
        |    +-- RecursionError
        +-- SyntaxError
        |    +-- IndentationError
        |         +-- TabError
        +-- SystemError
        +-- TypeError
        +-- ValueError
        |    +-- UnicodeError
        |         +-- UnicodeDecodeError
        |         +-- UnicodeEncodeError
        |         +-- UnicodeTranslateError
        +-- Warning
             +-- DeprecationWarning
             +-- PendingDeprecationWarning
             +-- RuntimeWarning
             +-- SyntaxWarning
             +-- UserWarning
             +-- FutureWarning
             +-- ImportWarning
             +-- UnicodeWarning
             +-- BytesWarning
             +-- EncodingWarning
             +-- ResourceWarning





## 예외처리

- try 문(statement) / except 절(clause)을 이용하여 예외 처리 가능
- try 문
  - 오류가 발생할 가능성이 있는 코드를 실행
  - 예외가 발생되지 않으면, except 없이 실행 종료
- except 절
  - 예외가 발생하면, except 절이 실행
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

### 작성 방법

```python
try:
	try 명령문
except 예외그룹-1 as 변수-1 :    #주의 : try문은 반듯시 한 개 이상의 except문이 필요
	예외처리 명령문 1
except 예외그룹-2 as 변수-2 :
	예외처리 명령문 2
finally:   # 선택사항
	finally명령문
```

예시

```python
num = input('숫자입력 :')
print(int(num))
# 숫자입력 :안녕
# ------
# ValueError Traceback (most recent call last)
# 1 num = input('숫자입력 :')
# ----> 2 print(int(num))
# ValueError: invalid literal for int() with base 10: '안녕'

try:
num = input('숫자입력 :')
print(int(num))
except ValueError:
print('숫자가 아닙니다')
```

정리

- try

  > 코드를 실행함

- except

  > try 문에서 예외가 발생 시 실행함

- else

  > try 문에서 예외가 발생하지 않으면 실행함

- finally

  > 예외 발생 여부와 관계없이 항상 실행함



## 예외 발생 시키기

### raise statement

> raise를 통해 예외를 강제로 발생

```python
raise
# -------
# RuntimeError Traceback (most recent call last)
# ----> 1 raise
# RuntimeError: No active exception to reraise
```

> 우리가 보는 모든 에러 메시지가 raise를 통해 에러를 발생 시켜 보여주는 것이다. 파이썬 내부 코드를 보면 무수히 많은  raise 존재!



